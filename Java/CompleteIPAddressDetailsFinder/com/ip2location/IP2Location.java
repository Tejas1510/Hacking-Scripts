package com.ip2location;

import java.net.InetAddress;
import java.net.Inet4Address;
import java.net.Inet6Address;
import java.net.UnknownHostException;
import java.io.*;
import java.util.*;
import java.util.regex.*;
import java.math.BigInteger;
import java.nio.ByteBuffer;
import java.nio.MappedByteBuffer;
import java.nio.ByteOrder;
import java.nio.channels.FileChannel;
import java.lang.StringBuffer; // JDK 1.4 does not support StringBuilder so can't use that
import java.text.DecimalFormat;
import java.text.NumberFormat;

/**
* This class performs the lookup of IP2Location data from an IP address by reading a BIN file.
* <p>
* Example usage scenarios:
* <ul>
*   <li>Redirect based on country</li>
*   <li>Digital rights management</li>
*   <li>Web log stats and analysis</li>
*   <li>Auto-selection of country on forms</li>
*   <li>Filter access from countries you do not do business with</li>
*   <li>Geo-targeting for increased sales and click-through</li>
*   <li>And much, much more!</li>
* </ul>
* <p>
* <b>Requirements:</b> Java SDK 1.4 or later<br>
* <p>
* Copyright (c) 2002-2020 IP2Location.com
* <p>
*
* @author IP2Location.com
* @version 8.5.0
*/
public class IP2Location {
	private static final Pattern pattern = Pattern.compile("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"); // IPv4
	private static final Pattern pattern2 = Pattern.compile("^([0-9A-F]{1,4}:){6}(0[0-9]+\\.|.*?\\.0[0-9]+).*$", Pattern.CASE_INSENSITIVE);
	private static final Pattern pattern3 = Pattern.compile("^[0-9]+$");
	private static final Pattern pattern4 = Pattern.compile("^(.*:)(([0-9]+\\.){3}[0-9]+)$");
	private static final Pattern pattern5 = Pattern.compile("^.*((:[0-9A-F]{1,4}){2})$");
	private static final Pattern pattern6 = Pattern.compile("^[0:]+((:[0-9A-F]{1,4}){1,2})$", Pattern.CASE_INSENSITIVE);
	private static final BigInteger MAX_IPV4_RANGE = new BigInteger("4294967295");
	private static final BigInteger MAX_IPV6_RANGE = new BigInteger("340282366920938463463374607431768211455");
	private static final BigInteger FROM_6TO4 = new BigInteger("42545680458834377588178886921629466624");
	private static final BigInteger TO_6TO4 = new BigInteger("42550872755692912415807417417958686719");
	private static final BigInteger FROM_TEREDO = new BigInteger("42540488161975842760550356425300246528");
	private static final BigInteger TO_TEREDO = new BigInteger("42540488241204005274814694018844196863");
	private static final BigInteger LAST_32BITS = new BigInteger("4294967295");
	
	private static final int COUNTRY_POSITION[] = {0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2};
	private static final int REGION_POSITION[] = {0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3};
	private static final int CITY_POSITION[] = {0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4};
	private static final int ISP_POSITION[] = {0, 0, 3, 0, 5, 0, 7, 5, 7, 0, 8, 0, 9, 0, 9, 0, 9, 0, 9, 7, 9, 0, 9, 7, 9};
	private static final int LATITUDE_POSITION[]  = {0, 0, 0, 0, 0, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5};
	private static final int LONGITUDE_POSITION[] = {0, 0, 0, 0, 0, 6, 6, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6};
	private static final int DOMAIN_POSITION[] = {0, 0, 0, 0, 0, 0, 0, 6, 8, 0, 9, 0, 10,0, 10, 0, 10, 0, 10, 8, 10, 0, 10, 8, 10};
	private static final int ZIPCODE_POSITION[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 0, 7, 7, 7, 0, 7, 0, 7, 7, 7, 0, 7};
	private static final int TIMEZONE_POSITION[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 7, 8, 8, 8, 7, 8, 0, 8, 8, 8, 0, 8};
	private static final int NETSPEED_POSITION[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 11,0, 11,8, 11, 0, 11, 0, 11, 0, 11};
	private static final int IDDCODE_POSITION[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 12, 0, 12, 0, 12, 9, 12, 0, 12};
	private static final int AREACODE_POSITION[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10 ,13 ,0, 13, 0, 13, 10, 13, 0, 13};
	private static final int WEATHERSTATIONCODE_POSITION[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 14, 0, 14, 0, 14, 0, 14};
	private static final int WEATHERSTATIONNAME_POSITION[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 15, 0, 15, 0, 15, 0, 15};
	private static final int MCC_POSITION[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 16, 0, 16, 9, 16};
	private static final int MNC_POSITION[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10,17, 0, 17, 10, 17};
	private static final int MOBILEBRAND_POSITION[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11,18, 0, 18, 11, 18};
	private static final int ELEVATION_POSITION[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 19, 0, 19};
	private static final int USAGETYPE_POSITION[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 20};
	// private static final DecimalFormat df = new DecimalFormat("###.######");
	private MetaData _MetaData = null;
	// private MappedByteBuffer _IndexBuffer = null;
	private MappedByteBuffer _IPv4Buffer = null;
	private MappedByteBuffer _IPv6Buffer = null;
	private MappedByteBuffer _MapDataBuffer = null;
	// private int _IndexOffset = 0;
	private int[][] _IndexArrayIPv4 = new int[65536][2];
	private int[][] _IndexArrayIPv6 = new int[65536][2];
	private long _IPv4Offset = 0;
	private long _IPv6Offset = 0;
	private long _MapDataOffset = 0;
	private int _IPv4ColumnSize = 0;
	private int _IPv6ColumnSize = 0;

/**
* To use memory mapped file for faster queries, set to true.
*/
	public boolean UseMemoryMappedFile = false;
/**
* Sets the path for the BIN database (IPv4 BIN or IPv4+IPv6 BIN).
*/
	public String IPDatabasePath = "";
/**
* Sets the path for the license key file.
*/
	public String IPLicensePath = "";
	private boolean gotdelay = false;
	// private boolean isdelayed = false;
	private boolean _alreadyCheckedKey = false;
	private int COUNTRY_POSITION_OFFSET;
	private int REGION_POSITION_OFFSET;
	private int CITY_POSITION_OFFSET;
	private int ISP_POSITION_OFFSET;
	private int DOMAIN_POSITION_OFFSET;
	private int ZIPCODE_POSITION_OFFSET;
	private int LATITUDE_POSITION_OFFSET;
	private int LONGITUDE_POSITION_OFFSET;
	private int TIMEZONE_POSITION_OFFSET;
	private int NETSPEED_POSITION_OFFSET;
	private int IDDCODE_POSITION_OFFSET;
	private int AREACODE_POSITION_OFFSET;
	private int WEATHERSTATIONCODE_POSITION_OFFSET;
	private int WEATHERSTATIONNAME_POSITION_OFFSET;
	private int MCC_POSITION_OFFSET;
	private int MNC_POSITION_OFFSET;
	private int MOBILEBRAND_POSITION_OFFSET;
	private int ELEVATION_POSITION_OFFSET;
	private int USAGETYPE_POSITION_OFFSET;
	private boolean COUNTRY_ENABLED;
	private boolean REGION_ENABLED;
	private boolean CITY_ENABLED;
	private boolean ISP_ENABLED;
	private boolean LATITUDE_ENABLED;
	private boolean LONGITUDE_ENABLED;
	private boolean DOMAIN_ENABLED;
	private boolean ZIPCODE_ENABLED;
	private boolean TIMEZONE_ENABLED;
	private boolean NETSPEED_ENABLED;
	private boolean IDDCODE_ENABLED;
	private boolean AREACODE_ENABLED;
	private boolean WEATHERSTATIONCODE_ENABLED;
	private boolean WEATHERSTATIONNAME_ENABLED;
	private boolean MCC_ENABLED;
	private boolean MNC_ENABLED;
	private boolean MOBILEBRAND_ENABLED;
	private boolean ELEVATION_ENABLED;
	private boolean USAGETYPE_ENABLED;
	
	public IP2Location() {
	
	}
	
	
	/**
	* This function can be used to pre-load the BIN file.
	*/
	public void Open(String DBPath) throws IOException {
		IPDatabasePath = DBPath;
		LoadBIN();
	}
	
	/**
	* This function can be used to initialized the component with params and pre-load the BIN file.
	*/
	public void Open(String DBPath, boolean UseMMF) throws IOException {
		UseMemoryMappedFile = UseMMF;
		Open(DBPath);
	}
	
	/**
	* This function destroys the mapped bytes.
	*/
	public void Close() {
		if (_MetaData != null) {
			_MetaData = null;
		}
		DestroyMappedBytes();
	}
	
	private void DestroyMappedBytes() {
		if (_IPv4Buffer != null) {
			_IPv4Buffer = null;
		}
		// if (_IndexBuffer != null) {
			// _IndexBuffer = null;
		// }
		if (_IPv6Buffer != null) {
			_IPv6Buffer = null;
		}
		if (_MapDataBuffer != null) {
			_MapDataBuffer = null;
		}
	}
	
	private void CreateMappedBytes() throws IOException {
		RandomAccessFile aFile = null; // shift here to address file handle exhaustion issue and NOT using FINAL variable
		// FileInputStream aFile = null;
		
		try {
			aFile = new RandomAccessFile(IPDatabasePath, "r");
			// aFile = new FileInputStream(IPDatabasePath);
			final FileChannel inChannel = aFile.getChannel();
			CreateMappedBytes(inChannel);
		}
		// catch (FileNotFoundException ex1) {
			// throw ex1;
		// }
		catch (IOException ex) { // includes FileNotFoundException
			throw ex;
		}
		finally {
			if (aFile != null) {
				aFile.close();
				aFile = null;
			}
		}
	}
	
	private void CreateMappedBytes(FileChannel inChannel) throws IOException {
		try {
			if (_IPv4Buffer == null) {
				final long _IPv4Bytes = (long)_IPv4ColumnSize * (long)_MetaData.getDBCount();
				_IPv4Offset = _MetaData.getBaseAddr() - 1;
				_IPv4Buffer = inChannel.map(FileChannel.MapMode.READ_ONLY, _IPv4Offset, _IPv4Bytes);
				_IPv4Buffer.order(ByteOrder.LITTLE_ENDIAN);
				_MapDataOffset = _IPv4Offset + _IPv4Bytes;
			}
			
			// NO LONGER USING BUFFER AS IT IS TOO SLOW, USING MULTI-DIMENSIONAL ARRAY NOW
			// if (_MetaData.getIndexed()) {
				// final int _IndexBytes = _MetaData.getBaseAddr() - _MetaData.getIndexBaseAddr();
				// _IndexOffset =  _MetaData.getIndexBaseAddr() - 1;
				// _IndexBuffer = inChannel.map(FileChannel.MapMode.READ_ONLY, _IndexOffset, _IndexBytes);
				// _IndexBuffer.order(ByteOrder.LITTLE_ENDIAN);
			// }
			
			if (!_MetaData.getOldBIN() && _IPv6Buffer == null) {
				final long _IPv6Bytes = (long)_IPv6ColumnSize * (long)_MetaData.getDBCountIPv6();
				_IPv6Offset = _MetaData.getBaseAddrIPv6() - 1;
				_IPv6Buffer = inChannel.map(FileChannel.MapMode.READ_ONLY, _IPv6Offset, _IPv6Bytes);
				_IPv6Buffer.order(ByteOrder.LITTLE_ENDIAN);
				_MapDataOffset = _IPv6Offset + _IPv6Bytes;
			}
			
			if (_MapDataBuffer == null) {
				_MapDataBuffer = inChannel.map(FileChannel.MapMode.READ_ONLY, _MapDataOffset, inChannel.size() - _MapDataOffset);
				_MapDataBuffer.order(ByteOrder.LITTLE_ENDIAN);
			}
		}
		// catch (FileNotFoundException ex1) {
			// throw ex1;
		// }
		catch (IOException ex) { // includes FileNotFoundException
			throw ex;
		}
	}
	
	private boolean LoadBIN() throws IOException {
		boolean loadOK = false;
		RandomAccessFile aFile = null; // shift here to address file handle exhaustion issue and NOT using FINAL variable
		// FileInputStream aFile = null;
		// FileInputStream aFile2 = null;
		
		try {
			if (IPDatabasePath.length() > 0) {
				aFile = new RandomAccessFile(IPDatabasePath, "r");
				// aFile = new FileInputStream(IPDatabasePath);
				final FileChannel inChannel = aFile.getChannel();
				final MappedByteBuffer _HeaderBuffer = inChannel.map(FileChannel.MapMode.READ_ONLY, 0, 64); // 64 bytes header
				// ByteBuffer _HeaderBuffer = ByteBuffer.allocate(64); // 64 bytes header
				// inChannel.read(_HeaderBuffer); // reading header
				
				_HeaderBuffer.order(ByteOrder.LITTLE_ENDIAN);
				// _HeaderBuffer.rewind();
				// System.out.println("Header position: " + _HeaderBuffer.position());
				// System.out.println("Header limit: " + _HeaderBuffer.limit());
				// System.out.println("Header capacity: " + _HeaderBuffer.capacity());
				_MetaData = new MetaData();
				
				_MetaData.setDBType(_HeaderBuffer.get(0));
				_MetaData.setDBColumn(_HeaderBuffer.get(1));
				_MetaData.setDBYear(_HeaderBuffer.get(2));
				_MetaData.setDBMonth(_HeaderBuffer.get(3));
				_MetaData.setDBDay(_HeaderBuffer.get(4));
				_MetaData.setDBCount(_HeaderBuffer.getInt(5)); // 4 bytes
				_MetaData.setBaseAddr(_HeaderBuffer.getInt(9)); // 4 bytes
				_MetaData.setDBCountIPv6(_HeaderBuffer.getInt(13)); // 4 bytes
				_MetaData.setBaseAddrIPv6(_HeaderBuffer.getInt(17)); // 4 bytes
				_MetaData.setIndexBaseAddr(_HeaderBuffer.getInt(21)); //4 bytes
				_MetaData.setIndexBaseAddrIPv6(_HeaderBuffer.getInt(25)); //4 bytes
				
				// _MetaData.setDBType(_HeaderBuffer.get());
				// _MetaData.setDBColumn(_HeaderBuffer.get());
				// _MetaData.setDBYear(_HeaderBuffer.get());
				// _MetaData.setDBMonth(_HeaderBuffer.get());
				// _MetaData.setDBDay(_HeaderBuffer.get());
				// _MetaData.setDBCount(_HeaderBuffer.getInt()); // 4 bytes
				// _MetaData.setBaseAddr(_HeaderBuffer.getInt()); // 4 bytes
				// _MetaData.setDBCountIPv6(_HeaderBuffer.getInt()); // 4 bytes
				// _MetaData.setBaseAddrIPv6(_HeaderBuffer.getInt()); // 4 bytes
				// _MetaData.setIndexBaseAddr(_HeaderBuffer.getInt()); //4 bytes
				// _MetaData.setIndexBaseAddrIPv6(_HeaderBuffer.getInt()); //4 bytes
				
				// _HeaderBuffer = null;
				
				if (_MetaData.getIndexBaseAddr() > 0) {
					_MetaData.setIndexed(true);
				}
				
				if (_MetaData.getDBCountIPv6() == 0) { // old style IPv4-only BIN file
					_MetaData.setOldBIN(true);
				}
				else {
					if (_MetaData.getIndexBaseAddrIPv6() > 0) {
						_MetaData.setIndexedIPv6(true);
					}
				}
					
				final int dbcoll = _MetaData.getDBColumn();
				_IPv4ColumnSize = dbcoll << 2; // 4 bytes each column
				_IPv6ColumnSize = 16 + ((dbcoll - 1) << 2); // 4 bytes each column, except IPFrom column which is 16 bytes
				
				final int dbtype = _MetaData.getDBType();
				
				// since both IPv4 and IPv6 use 4 bytes for the below columns, can just do it once here
				// COUNTRY_POSITION_OFFSET = (COUNTRY_POSITION[dbtype] != 0) ? (COUNTRY_POSITION[dbtype] - 1) << 2 : 0;
				// REGION_POSITION_OFFSET = (REGION_POSITION[dbtype] != 0) ? (REGION_POSITION[dbtype] - 1) << 2 : 0;
				// CITY_POSITION_OFFSET = (CITY_POSITION[dbtype] != 0) ? (CITY_POSITION[dbtype] - 1) << 2 : 0;
				// ISP_POSITION_OFFSET = (ISP_POSITION[dbtype] != 0) ? (ISP_POSITION[dbtype] - 1) << 2 : 0;
				// DOMAIN_POSITION_OFFSET = (DOMAIN_POSITION[dbtype] != 0) ? (DOMAIN_POSITION[dbtype] - 1) << 2 : 0;
				// ZIPCODE_POSITION_OFFSET = (ZIPCODE_POSITION[dbtype] != 0) ? (ZIPCODE_POSITION[dbtype] - 1) << 2 : 0;
				// LATITUDE_POSITION_OFFSET = (LATITUDE_POSITION[dbtype] != 0) ? (LATITUDE_POSITION[dbtype] - 1) << 2 : 0;
				// LONGITUDE_POSITION_OFFSET = (LONGITUDE_POSITION[dbtype] != 0) ? (LONGITUDE_POSITION[dbtype] - 1) << 2 : 0;
				// TIMEZONE_POSITION_OFFSET = (TIMEZONE_POSITION[dbtype] != 0) ? (TIMEZONE_POSITION[dbtype] - 1) << 2 : 0;
				// NETSPEED_POSITION_OFFSET = (NETSPEED_POSITION[dbtype] != 0) ? (NETSPEED_POSITION[dbtype] - 1) << 2 : 0;
				// IDDCODE_POSITION_OFFSET = (IDDCODE_POSITION[dbtype] != 0) ? (IDDCODE_POSITION[dbtype] - 1) << 2 : 0;
				// AREACODE_POSITION_OFFSET = (AREACODE_POSITION[dbtype] != 0) ? (AREACODE_POSITION[dbtype] - 1) << 2 : 0;
				// WEATHERSTATIONCODE_POSITION_OFFSET = (WEATHERSTATIONCODE_POSITION[dbtype] != 0) ? (WEATHERSTATIONCODE_POSITION[dbtype] - 1) << 2 : 0;
				// WEATHERSTATIONNAME_POSITION_OFFSET = (WEATHERSTATIONNAME_POSITION[dbtype] != 0) ? (WEATHERSTATIONNAME_POSITION[dbtype] - 1) << 2 : 0;
				// MCC_POSITION_OFFSET = (MCC_POSITION[dbtype] != 0) ? (MCC_POSITION[dbtype] - 1) << 2 : 0;
				// MNC_POSITION_OFFSET = (MNC_POSITION[dbtype] != 0) ? (MNC_POSITION[dbtype] - 1) << 2 : 0;
				// MOBILEBRAND_POSITION_OFFSET = (MOBILEBRAND_POSITION[dbtype] != 0) ? (MOBILEBRAND_POSITION[dbtype] - 1) << 2 : 0;
				// ELEVATION_POSITION_OFFSET = (ELEVATION_POSITION[dbtype] != 0) ? (ELEVATION_POSITION[dbtype] - 1) << 2 : 0;
				// USAGETYPE_POSITION_OFFSET = (USAGETYPE_POSITION[dbtype] != 0) ? (USAGETYPE_POSITION[dbtype] - 1) << 2 : 0;
				
				// slightly different offset for reading by row
				COUNTRY_POSITION_OFFSET = (COUNTRY_POSITION[dbtype] != 0) ? (COUNTRY_POSITION[dbtype] - 2) << 2 : 0;
				REGION_POSITION_OFFSET = (REGION_POSITION[dbtype] != 0) ? (REGION_POSITION[dbtype] - 2) << 2 : 0;
				CITY_POSITION_OFFSET = (CITY_POSITION[dbtype] != 0) ? (CITY_POSITION[dbtype] - 2) << 2 : 0;
				ISP_POSITION_OFFSET = (ISP_POSITION[dbtype] != 0) ? (ISP_POSITION[dbtype] - 2) << 2 : 0;
				DOMAIN_POSITION_OFFSET = (DOMAIN_POSITION[dbtype] != 0) ? (DOMAIN_POSITION[dbtype] - 2) << 2 : 0;
				ZIPCODE_POSITION_OFFSET = (ZIPCODE_POSITION[dbtype] != 0) ? (ZIPCODE_POSITION[dbtype] - 2) << 2 : 0;
				LATITUDE_POSITION_OFFSET = (LATITUDE_POSITION[dbtype] != 0) ? (LATITUDE_POSITION[dbtype] - 2) << 2 : 0;
				LONGITUDE_POSITION_OFFSET = (LONGITUDE_POSITION[dbtype] != 0) ? (LONGITUDE_POSITION[dbtype] - 2) << 2 : 0;
				TIMEZONE_POSITION_OFFSET = (TIMEZONE_POSITION[dbtype] != 0) ? (TIMEZONE_POSITION[dbtype] - 2) << 2 : 0;
				NETSPEED_POSITION_OFFSET = (NETSPEED_POSITION[dbtype] != 0) ? (NETSPEED_POSITION[dbtype] - 2) << 2 : 0;
				IDDCODE_POSITION_OFFSET = (IDDCODE_POSITION[dbtype] != 0) ? (IDDCODE_POSITION[dbtype] - 2) << 2 : 0;
				AREACODE_POSITION_OFFSET = (AREACODE_POSITION[dbtype] != 0) ? (AREACODE_POSITION[dbtype] - 2) << 2 : 0;
				WEATHERSTATIONCODE_POSITION_OFFSET = (WEATHERSTATIONCODE_POSITION[dbtype] != 0) ? (WEATHERSTATIONCODE_POSITION[dbtype] - 2) << 2 : 0;
				WEATHERSTATIONNAME_POSITION_OFFSET = (WEATHERSTATIONNAME_POSITION[dbtype] != 0) ? (WEATHERSTATIONNAME_POSITION[dbtype] - 2) << 2 : 0;
				MCC_POSITION_OFFSET = (MCC_POSITION[dbtype] != 0) ? (MCC_POSITION[dbtype] - 2) << 2 : 0;
				MNC_POSITION_OFFSET = (MNC_POSITION[dbtype] != 0) ? (MNC_POSITION[dbtype] - 2) << 2 : 0;
				MOBILEBRAND_POSITION_OFFSET = (MOBILEBRAND_POSITION[dbtype] != 0) ? (MOBILEBRAND_POSITION[dbtype] - 2) << 2 : 0;
				ELEVATION_POSITION_OFFSET = (ELEVATION_POSITION[dbtype] != 0) ? (ELEVATION_POSITION[dbtype] - 2) << 2 : 0;
				USAGETYPE_POSITION_OFFSET = (USAGETYPE_POSITION[dbtype] != 0) ? (USAGETYPE_POSITION[dbtype] - 2) << 2 : 0;
				
				COUNTRY_ENABLED = (COUNTRY_POSITION[dbtype]!=0) ? true : false;
				REGION_ENABLED = (REGION_POSITION[dbtype]!=0) ? true : false;
				CITY_ENABLED = (CITY_POSITION[dbtype]!=0) ? true : false;
				ISP_ENABLED = (ISP_POSITION[dbtype]!=0) ? true : false;
				LATITUDE_ENABLED = (LATITUDE_POSITION[dbtype]!=0) ? true : false;
				LONGITUDE_ENABLED = (LONGITUDE_POSITION[dbtype]!=0) ? true : false;
				DOMAIN_ENABLED = (DOMAIN_POSITION[dbtype]!=0) ? true : false;
				ZIPCODE_ENABLED = (ZIPCODE_POSITION[dbtype]!=0) ? true : false;
				TIMEZONE_ENABLED = (TIMEZONE_POSITION[dbtype]!=0) ? true : false;
				NETSPEED_ENABLED = (NETSPEED_POSITION[dbtype]!=0) ? true : false;
				IDDCODE_ENABLED = (IDDCODE_POSITION[dbtype]!=0) ? true : false;
				AREACODE_ENABLED = (AREACODE_POSITION[dbtype]!=0) ? true : false;
				WEATHERSTATIONCODE_ENABLED = (WEATHERSTATIONCODE_POSITION[dbtype]!=0) ? true : false;
				WEATHERSTATIONNAME_ENABLED = (WEATHERSTATIONNAME_POSITION[dbtype]!=0) ? true : false;
				MCC_ENABLED = (MCC_POSITION[dbtype]!=0) ? true : false;
				MNC_ENABLED = (MNC_POSITION[dbtype]!=0) ? true : false;
				MOBILEBRAND_ENABLED = (MOBILEBRAND_POSITION[dbtype]!=0) ? true : false;
				ELEVATION_ENABLED = (ELEVATION_POSITION[dbtype]!=0) ? true : false;
				USAGETYPE_ENABLED = (USAGETYPE_POSITION[dbtype]!=0) ? true : false;
				
				if (_MetaData.getIndexed()) {
					// aFile2 = new FileInputStream(IPDatabasePath);
					// inChannel = aFile2.getChannel();
					
					final MappedByteBuffer _IndexBuffer = inChannel.map(FileChannel.MapMode.READ_ONLY, _MetaData.getIndexBaseAddr() - 1, _MetaData.getBaseAddr() - _MetaData.getIndexBaseAddr()); // reading indexes
					// ByteBuffer _IndexBuffer = ByteBuffer.allocate(_MetaData.getBaseAddr() - _MetaData.getIndexBaseAddr());
					// inChannel.read(_IndexBuffer, _MetaData.getIndexBaseAddr() - 1); // reading indexes from start of index
					_IndexBuffer.order(ByteOrder.LITTLE_ENDIAN);
					// _IndexBuffer.rewind();
					int pointer = 0;
					
					// read IPv4 index
					for (int x = 0; x < _IndexArrayIPv4.length; x++) {
						_IndexArrayIPv4[x][0] = _IndexBuffer.getInt(pointer); // 4 bytes for from row
						_IndexArrayIPv4[x][1] = _IndexBuffer.getInt(pointer + 4); // 4 bytes for to row
						pointer += 8;
						// _IndexArrayIPv4[x][0] = _IndexBuffer.getInt(); // 4 bytes for from row
						// _IndexArrayIPv4[x][1] = _IndexBuffer.getInt(); // 4 bytes for to row
					}
					
					if (_MetaData.getIndexedIPv6()) {
						// read IPv6 index
						for (int x = 0; x < _IndexArrayIPv6.length; x++) {
							_IndexArrayIPv6[x][0] = _IndexBuffer.getInt(pointer); // 4 bytes for from row
							_IndexArrayIPv6[x][1] = _IndexBuffer.getInt(pointer + 4); // 4 bytes for to row
							pointer += 8;
							// _IndexArrayIPv6[x][0] = _IndexBuffer.getInt(); // 4 bytes for from row
							// _IndexArrayIPv6[x][1] = _IndexBuffer.getInt(); // 4 bytes for to row
						}
					}
					// _IndexBuffer = null;
				}
				
				if (UseMemoryMappedFile) {
					CreateMappedBytes(inChannel);
				}
				else {
					DestroyMappedBytes();
				}
				loadOK = true;
			}
		}
		catch(IOException ex) {
			throw ex;
		}
		finally {
			if (aFile != null) {
				aFile.close();
				aFile = null;
			}
		}
		return loadOK;
	}
	
/**
* @deprecated
*/
	protected void finalize() throws Throwable {
		super.finalize();
	}
	
/**
* This function to query IP2Location data.
* @param IPAddress IP Address you wish to query
* @return IP2Location data
*/
	public IPResult IPQuery(String IPAddress) throws IOException {
		IPAddress = IPAddress.trim();
		IPResult record = new IPResult(IPAddress);
		RandomAccessFile filehandle = null;
		// MappedByteBuffer mybuffer = null;
		ByteBuffer mybuffer = null;
		ByteBuffer mydatabuffer = null;
		
		try {
			if (IPAddress == null || IPAddress.length() == 0) {
				record.status = "EMPTY_IP_ADDRESS";
				return record;
			}
			
			BigInteger ipno;
			// BigInteger ipno2;
			int indexaddr = 0;
			int actualiptype = 0;
			int myiptype = 0;
			int mydbtype = 0;
			int mybaseaddr = 0;
			int mydbcolumn = 0;
			int mycolumnsize = 0;
			int mybufcapacity = 0;
			BigInteger MAX_IP_RANGE = BigInteger.ZERO;
			long rowoffset = 0;
			long rowoffset2 = 0;
			BigInteger[] bi;
			boolean overcapacity = false;
			String[] retarr;
			
			try {
				bi = ip2no(IPAddress);
				myiptype = bi[0].intValue();
				ipno = bi[1];
				actualiptype = bi[2].intValue();
				if (actualiptype == 6) { // means didn't match IPv4 regex
					retarr = ExpandIPv6(IPAddress, myiptype);
					record.ip_address = retarr[0]; // return after expand IPv6 format
					myiptype = Integer.parseInt(retarr[1]); // special cases
				}
			}
			catch(UnknownHostException e) {
				record.status = "INVALID_IP_ADDRESS";
				return record;
			}
			
			long low = 0;
			long high = 0;
			long mid = 0;
			long position = 0;
			BigInteger ipfrom = BigInteger.ZERO;
			BigInteger ipto = BigInteger.ZERO;
			
			// Read BIN if haven't done so
			if (_MetaData == null) {
				if (!LoadBIN()) { // problems reading BIN
					record.status = "MISSING_FILE";
					return record;
				}
			}
			
			// mydbtype = _MetaData.getDBType();
			// mydbcolumn = _MetaData.getDBColumn();
			
			if (UseMemoryMappedFile) {
				if ((_IPv4Buffer == null) || (!_MetaData.getOldBIN() && _IPv6Buffer == null) || (_MapDataBuffer == null)) {
					CreateMappedBytes();
				}
			}
			else {
				DestroyMappedBytes();
				filehandle = new RandomAccessFile(IPDatabasePath, "r");
				
				if (filehandle == null) {
					record.status = "MISSING_FILE";
					return record;
				}
			}
			
			if (myiptype == 4) { // IPv4
				MAX_IP_RANGE = MAX_IPV4_RANGE;
				high = _MetaData.getDBCount();
				
				if (UseMemoryMappedFile) {
					// mybuffer = _IPv4Buffer;
					mybuffer = _IPv4Buffer.duplicate(); // this enables this thread to maintain its own position in a multi-threaded environment
					mybuffer.order(ByteOrder.LITTLE_ENDIAN);
					mybufcapacity = mybuffer.capacity();
				}
				else {
					mybaseaddr = _MetaData.getBaseAddr();
				}
				mycolumnsize = _IPv4ColumnSize;
				
				if (_MetaData.getIndexed()) {
					// ipno2 = ipno;
					// ipno2 = ipno2.shiftRight(16); //get the first 2 octets
					// indexaddr = ipno2.shiftLeft(3).longValue(); //4 bytes for from row & 4 bytes for to row
					// indexaddr = ipno.shiftRight(16).shiftLeft(3).longValue(); //old style for buffer
					indexaddr = ipno.shiftRight(16).intValue(); //new style for array
					
					// if (!UseMemoryMappedFile) {
						// indexaddr += _MetaData.getIndexBaseAddr();
					// }
					// low = read32(indexaddr, _IndexBuffer, filehandle).longValue(); //4 bytes
					// high = read32(indexaddr + 4, _IndexBuffer, filehandle).longValue(); //4 bytes
					low = _IndexArrayIPv4[indexaddr][0];
					high = _IndexArrayIPv4[indexaddr][1];
				}
			}
			else { // IPv6
				if (_MetaData.getOldBIN()) {
					record.status = "IPV6_NOT_SUPPORTED";
					return record;
				}
				MAX_IP_RANGE = MAX_IPV6_RANGE;
				high = _MetaData.getDBCountIPv6();
				
				if (UseMemoryMappedFile) {
					// mybuffer = _IPv6Buffer;
					mybuffer = _IPv6Buffer.duplicate(); // this enables this thread to maintain its own position in a multi-threaded environment
					mybuffer.order(ByteOrder.LITTLE_ENDIAN);
					mybufcapacity = mybuffer.capacity();
				}
				else {
					mybaseaddr = _MetaData.getBaseAddrIPv6();
				}
				mycolumnsize = _IPv6ColumnSize;
				
				if (_MetaData.getIndexedIPv6()) {
					// ipno2 = ipno;
					// ipno2 = ipno2.shiftRight(112); //get the first 2 octets
					// indexaddr = ipno2.shiftLeft(3).longValue(); //4 bytes for from row & 4 bytes for to row
					// indexaddr = ipno.shiftRight(112).shiftLeft(3).longValue(); //old style for buffer
					indexaddr = ipno.shiftRight(112).intValue(); //new style for array
					
					// if (!UseMemoryMappedFile) {
						// indexaddr += _MetaData.getIndexBaseAddrIPv6();
					// }
					// else {
						// indexaddr += (_MetaData.getIndexBaseAddrIPv6() - _MetaData.getIndexBaseAddr()); //IPv6 index always follows IPv4 index so offset IPv4 first
					// }
					// low = read32(indexaddr, _IndexBuffer, filehandle).longValue(); //4 bytes
					// high = read32(indexaddr + 4, _IndexBuffer, filehandle).longValue(); //4 bytes
					low = _IndexArrayIPv6[indexaddr][0];
					high = _IndexArrayIPv6[indexaddr][1];
				}
			}
			
			if (ipno.compareTo(MAX_IP_RANGE) == 0) ipno = ipno.subtract(BigInteger.ONE);
			
			while (low <= high) {
				mid = (long)((low + high)/2);
				rowoffset = mybaseaddr + (mid * mycolumnsize);
				rowoffset2 = rowoffset + mycolumnsize;
				
				if (UseMemoryMappedFile) {
					overcapacity = (rowoffset2 >= mybufcapacity);
				}
				
				ipfrom = read32or128(rowoffset, myiptype, mybuffer, filehandle);
				ipto = (overcapacity) ? BigInteger.ZERO : read32or128(rowoffset2, myiptype, mybuffer, filehandle);
				
				if (ipno.compareTo(ipfrom) >= 0 && ipno.compareTo(ipto) < 0) {
					// System.out.println("ipno: " + ipno + " ipfrom : " + ipfrom + " ipto: " + ipto);
					int firstcol = 4; // IP From is 4 bytes
					if (myiptype == 6) { // IPv6
						firstcol = 16; // IPv6 is 16 bytes
						// rowoffset = rowoffset + 12; // coz below is assuming all columns are 4 bytes, so got 12 left to go to make 16 bytes total
					}
					
					// read the row here after the IP From column (remaining columns are all 4 bytes)
					int rowlen = mycolumnsize - firstcol;
					byte[] row;
					row = readrow(rowoffset + firstcol, rowlen, mybuffer, filehandle);
					
					if (UseMemoryMappedFile) {
						mydatabuffer = _MapDataBuffer.duplicate(); // this is to enable reading of a range of bytes in multi-threaded environment
						mydatabuffer.order(ByteOrder.LITTLE_ENDIAN);
					}
					
					if (COUNTRY_ENABLED) {
						// position = read32(rowoffset + COUNTRY_POSITION_OFFSET, mybuffer, filehandle).longValue();
						position = read32_row(row, COUNTRY_POSITION_OFFSET).longValue();
						// record.country_short = readStr(position, filehandle);
						record.country_short = readStr(position, mydatabuffer, filehandle);
						position += 3;
						// record.country_long = readStr(position, filehandle);
						record.country_long = readStr(position, mydatabuffer, filehandle);
					}
					else {
						record.country_short = IPResult.NOT_SUPPORTED;
						record.country_long = IPResult.NOT_SUPPORTED;
					}
					if (REGION_ENABLED) {
						// position = read32(rowoffset + REGION_POSITION_OFFSET, mybuffer, filehandle).longValue();
						position = read32_row(row, REGION_POSITION_OFFSET).longValue();
						// record.region = readStr(position, filehandle);
						record.region = readStr(position, mydatabuffer, filehandle);
					}
					else {
						record.region = IPResult.NOT_SUPPORTED;
					}
					if (CITY_ENABLED) {
						// position = read32(rowoffset + CITY_POSITION_OFFSET, mybuffer, filehandle).longValue();
						position = read32_row(row, CITY_POSITION_OFFSET).longValue();
						// record.city = readStr(position, filehandle);
						record.city = readStr(position, mydatabuffer, filehandle);
					}
					else {
						record.city = IPResult.NOT_SUPPORTED;
					}
					if (ISP_ENABLED) {
						// position = read32(rowoffset + ISP_POSITION_OFFSET, mybuffer, filehandle).longValue();
						position = read32_row(row, ISP_POSITION_OFFSET).longValue();
						// record.isp = readStr(position, filehandle);
						record.isp = readStr(position, mydatabuffer, filehandle);
					}
					else {
						record.isp = IPResult.NOT_SUPPORTED;
					}
					if (LATITUDE_ENABLED) {
						// position = rowoffset + LATITUDE_POSITION_OFFSET;
						// record.latitude = readFloat(position, mybuffer, filehandle);
						// new requirement to "round" to 6 decimals
						// record.latitude = Float.parseFloat(df.format(readFloat(position, mybuffer, filehandle)));
						// record.latitude = Float.parseFloat(setDecimalPlaces(readFloat(position, mybuffer, filehandle)));
						record.latitude = Float.parseFloat(setDecimalPlaces(readFloat_row(row, LATITUDE_POSITION_OFFSET)));
					}
					else {
						record.latitude = 0.0F;
					}
					if (LONGITUDE_ENABLED) {
						// position = rowoffset + LONGITUDE_POSITION_OFFSET;
						// record.longitude = readFloat(position, mybuffer, filehandle);
						// new requirement to "round" to 6 decimals
						// record.longitude = Float.parseFloat(setDecimalPlaces(readFloat(position, mybuffer, filehandle)));
						record.longitude = Float.parseFloat(setDecimalPlaces(readFloat_row(row, LONGITUDE_POSITION_OFFSET)));
					}
					else {
						record.longitude = 0.0F;
					}
					if (DOMAIN_ENABLED) {
						// position = read32(rowoffset + DOMAIN_POSITION_OFFSET, mybuffer, filehandle).longValue();
						position = read32_row(row, DOMAIN_POSITION_OFFSET).longValue();
						// record.domain = readStr(position, filehandle);
						record.domain = readStr(position, mydatabuffer, filehandle);
					}
					else {
						record.domain = IPResult.NOT_SUPPORTED;
					}
					if (ZIPCODE_ENABLED) {
						// position = read32(rowoffset + ZIPCODE_POSITION_OFFSET, mybuffer, filehandle).longValue();
						position = read32_row(row, ZIPCODE_POSITION_OFFSET).longValue();
						// record.zipcode = readStr(position, filehandle);
						record.zipcode = readStr(position, mydatabuffer, filehandle);
					}
					else {
						record.zipcode = IPResult.NOT_SUPPORTED;
					}
					if (TIMEZONE_ENABLED) {
						// position = read32(rowoffset + TIMEZONE_POSITION_OFFSET, mybuffer, filehandle).longValue();
						position = read32_row(row, TIMEZONE_POSITION_OFFSET).longValue();
						// record.timezone = readStr(position, filehandle);
						record.timezone = readStr(position, mydatabuffer, filehandle);
					}
					else {
						record.timezone = IPResult.NOT_SUPPORTED;
					}
					if (NETSPEED_ENABLED) {
						// position = read32(rowoffset + NETSPEED_POSITION_OFFSET, mybuffer, filehandle).longValue();
						position = read32_row(row, NETSPEED_POSITION_OFFSET).longValue();
						// record.netspeed = readStr(position, filehandle);
						record.netspeed = readStr(position, mydatabuffer, filehandle);
					}
					else {
						record.netspeed = IPResult.NOT_SUPPORTED;
					}
					if (IDDCODE_ENABLED) {
						// position = read32(rowoffset + IDDCODE_POSITION_OFFSET, mybuffer, filehandle).longValue();
						position = read32_row(row, IDDCODE_POSITION_OFFSET).longValue();
						// record.iddcode = readStr(position, filehandle);
						record.iddcode = readStr(position, mydatabuffer, filehandle);
					}
					else {
						record.iddcode = IPResult.NOT_SUPPORTED;
					}
					if (AREACODE_ENABLED) {
						// position = read32(rowoffset + AREACODE_POSITION_OFFSET, mybuffer, filehandle).longValue();
						position = read32_row(row, AREACODE_POSITION_OFFSET).longValue();
						// record.areacode = readStr(position, filehandle);
						record.areacode = readStr(position, mydatabuffer, filehandle);
					}
					else {
						record.areacode = IPResult.NOT_SUPPORTED;
					}
					if (WEATHERSTATIONCODE_ENABLED) {
						// position = read32(rowoffset + WEATHERSTATIONCODE_POSITION_OFFSET, mybuffer, filehandle).longValue();
						position = read32_row(row, WEATHERSTATIONCODE_POSITION_OFFSET).longValue();
						// record.weatherstationcode = readStr(position, filehandle);
						record.weatherstationcode = readStr(position, mydatabuffer, filehandle);
					}
					else {
						record.weatherstationcode = IPResult.NOT_SUPPORTED;
					}
					if (WEATHERSTATIONNAME_ENABLED) {
						// position = read32(rowoffset + WEATHERSTATIONNAME_POSITION_OFFSET, mybuffer, filehandle).longValue();
						position = read32_row(row, WEATHERSTATIONNAME_POSITION_OFFSET).longValue();
						// record.weatherstationname = readStr(position, filehandle);
						record.weatherstationname = readStr(position, mydatabuffer, filehandle);
					}
					else {
						record.weatherstationname = IPResult.NOT_SUPPORTED;
					}
					if (MCC_ENABLED) {
						// position = read32(rowoffset + MCC_POSITION_OFFSET, mybuffer, filehandle).longValue();
						position = read32_row(row, MCC_POSITION_OFFSET).longValue();
						// record.mcc = readStr(position, filehandle);
						record.mcc = readStr(position, mydatabuffer, filehandle);
					}
					else {
						record.mcc = IPResult.NOT_SUPPORTED;
					}
					if (MNC_ENABLED) {
						// position = read32(rowoffset + MNC_POSITION_OFFSET, mybuffer, filehandle).longValue();
						position = read32_row(row, MNC_POSITION_OFFSET).longValue();
						// record.mnc = readStr(position, filehandle);
						record.mnc = readStr(position, mydatabuffer, filehandle);
					}
					else {
						record.mnc = IPResult.NOT_SUPPORTED;
					}
					if (MOBILEBRAND_ENABLED) {
						// position = read32(rowoffset + MOBILEBRAND_POSITION_OFFSET, mybuffer, filehandle).longValue();
						position = read32_row(row, MOBILEBRAND_POSITION_OFFSET).longValue();
						// record.mobilebrand = readStr(position, filehandle);
						record.mobilebrand = readStr(position, mydatabuffer, filehandle);
					}
					else {
						record.mobilebrand = IPResult.NOT_SUPPORTED;
					}
					if (ELEVATION_ENABLED) {
						// position = read32(rowoffset + ELEVATION_POSITION_OFFSET, mybuffer, filehandle).longValue();
						position = read32_row(row, ELEVATION_POSITION_OFFSET).longValue();
						// record.elevation = convertFloat(readStr(position, filehandle)); // due to value being stored as a string but output as float
						record.elevation = convertFloat(readStr(position, mydatabuffer, filehandle)); // due to value being stored as a string but output as float
					}
					else {
						record.elevation = 0.0F;
					}
					if (USAGETYPE_ENABLED) {
						// position = read32(rowoffset + USAGETYPE_POSITION_OFFSET, mybuffer, filehandle).longValue();
						position = read32_row(row, USAGETYPE_POSITION_OFFSET).longValue();
						// record.usagetype = readStr(position, filehandle);
						record.usagetype = readStr(position, mydatabuffer, filehandle);
					}
					else {
						record.usagetype = IPResult.NOT_SUPPORTED;
					}
					record.status = "OK";
					break;
				}
				else {
					if (ipno.compareTo(ipfrom) < 0) {
						high = mid - 1;
					}
					else {
						low = mid + 1;
					}
				}
			}
			return record;
		}
		catch(IOException ex) {
			// ex.printStackTrace(System.out);
			throw ex;
		}
		finally {
			if (filehandle != null) {
				filehandle.close();
				filehandle = null;
			}
		}
	}
	
	private String[] ExpandIPv6(final String myIP, final int myiptype) {
		final String tmp = "0000:0000:0000:0000:0000:";
		final String padme = "0000";
		final long hexoffset = 0xFF;
		String myIP2 = myIP.toUpperCase();
		String rettype = String.valueOf(myiptype);
		
		// expand ipv4-mapped ipv6
		if (myiptype == 4) {
			if (pattern4.matcher(myIP2).matches()) {
				myIP2 = myIP2.replaceAll("::", tmp);
			}
			else {
				Matcher mat = pattern5.matcher(myIP2);
				
				if (mat.matches()) {
					String mymatch = mat.group(1);
					
					String[] myarr = mymatch.replaceAll("^:+", "").replaceAll(":+$", "").split(":");
					
					int len = myarr.length;
					StringBuffer bf = new StringBuffer(32);
					for (int x = 0; x < len; x++) {
						String unpadded = myarr[x];
						bf.append(padme.substring(unpadded.length()) + unpadded); // safe padding for JDK 1.4
					}
					long mylong = new BigInteger(bf.toString(), 16).longValue();
					
					long[] b = {0, 0, 0, 0}; // using long in place of bytes due to 2's complement signed issue
					
					for (int x = 0; x < 4; x++) {
						b[x] = mylong & hexoffset;
						mylong = mylong >> 8;
					}
					
					myIP2 = myIP2.replaceAll(mymatch + "$", ":" + b[3] + "." + b[2] + "." + b[1] + "." + b[0]);
					myIP2 = myIP2.replaceAll("::", tmp);
				}
				else {
				}
			}
		}
		else if (myiptype == 6) {
			if (myIP2.equals("::")) {
				myIP2 = myIP2 + "0.0.0.0";
				myIP2 = myIP2.replaceAll("::", tmp + "FFFF:");
				rettype = "4";
			}
			else {
				// same regex as myiptype 4 but different scenario
				Matcher mat = pattern4.matcher(myIP2);
				 if (mat.matches()) {
					String v6part = mat.group(1);
					String v4part = mat.group(2);
					
					String[] v4arr = v4part.split("\\.");
					int[] v4intarr = new int[4];
					
					int len = v4intarr.length;
					for (int x = 0; x < len; x++) {
						v4intarr[x] = Integer.parseInt(v4arr[x]);
					}
					int part1 = (v4intarr[0] << 8) + v4intarr[1];
					int part2 = (v4intarr[2] << 8) + v4intarr[3];
					String part1hex = Integer.toHexString(part1);
					String part2hex = Integer.toHexString(part2);
					
					StringBuffer bf = new StringBuffer(v6part.length() + 9);
					bf.append(v6part);
					bf.append(padme.substring(part1hex.length()));
					bf.append(part1hex);
					bf.append(":");
					bf.append(padme.substring(part2hex.length()));
					bf.append(part2hex);
					
					myIP2 = bf.toString().toUpperCase();
					
					String[] myarr = myIP2.split("::");
					
					String[] leftside = myarr[0].split(":");
					
					StringBuffer bf2 = new StringBuffer(40);
					StringBuffer bf3 = new StringBuffer(40);
					StringBuffer bf4 = new StringBuffer(40);
					
					len = leftside.length;
					int totalsegments = 0;
					for (int x = 0; x < len; x++) {
						if (leftside[x].length() > 0) {
							totalsegments++;
							bf2.append(padme.substring(leftside[x].length()));
							bf2.append(leftside[x]);
							bf2.append(":");
						}
					}
					
					if (myarr.length > 1) {
						String[] rightside = myarr[1].split(":");
						
						len = rightside.length;
						for (int x = 0; x < len; x++) {
							if (rightside[x].length() > 0) {
								totalsegments++;
								bf3.append(padme.substring(rightside[x].length()));
								bf3.append(rightside[x]);
								bf3.append(":");
							}
						}
					}
					
					int totalsegmentsleft = 8 - totalsegments;
					
					if (totalsegmentsleft == 6) {
						for (int x = 1; x < totalsegmentsleft; x++) {
							bf4.append(padme);
							bf4.append(":");
						}
						bf4.append("FFFF:");
						bf4.append(v4part);
						rettype = "4";
						myIP2 = bf4.toString();
					}
					else {
						for (int x = 0; x < totalsegmentsleft; x++) {
							bf4.append(padme);
							bf4.append(":");
						}
						bf2.append(bf4).append(bf3);
						myIP2 = bf2.toString().replaceAll(":$", "");
					}
					
				}
				else {
					// expand IPv4-compatible IPv6
					Matcher mat2 = pattern6.matcher(myIP2);
					
					if (mat2.matches()) {
						String mymatch = mat2.group(1);
						String[] myarr = mymatch.replaceAll("^:+", "").replaceAll(":+$", "").split(":");
						
						int len = myarr.length;
						StringBuffer bf = new StringBuffer(32);
						for (int x = 0; x < len; x++) {
							String unpadded = myarr[x];
							bf.append(padme.substring(unpadded.length()) + unpadded); // safe padding for JDK 1.4
						}
						
						long mylong = new BigInteger(bf.toString(), 16).longValue();
						
						long[] b = {0, 0, 0, 0}; // using long in place of bytes due to 2's complement signed issue
						
						for (int x = 0; x < 4; x++) {
							b[x] = mylong & hexoffset;
							mylong = mylong >> 8;
						}
						
						myIP2 = myIP2.replaceAll(mymatch + "$", ":" + b[3] + "." + b[2] + "." + b[1] + "." + b[0]);
						myIP2 = myIP2.replaceAll("::", tmp + "FFFF:");
						rettype = "4";
					}
					else {
						// should be normal IPv6 case
						String[] myarr = myIP2.split("::");
						
						String[] leftside = myarr[0].split(":");
						
						StringBuffer bf2 = new StringBuffer(40);
						StringBuffer bf3 = new StringBuffer(40);
						StringBuffer bf4 = new StringBuffer(40);
						
						int len = leftside.length;
						int totalsegments = 0;
						for (int x = 0; x < len; x++) {
							if (leftside[x].length() > 0) {
								totalsegments++;
								bf2.append(padme.substring(leftside[x].length()));
								bf2.append(leftside[x]);
								bf2.append(":");
							}
						}
						
						if (myarr.length > 1) {
							String[] rightside = myarr[1].split(":");
							
							len = rightside.length;
							for (int x = 0; x < len; x++) {
								if (rightside[x].length() > 0) {
									totalsegments++;
									bf3.append(padme.substring(rightside[x].length()));
									bf3.append(rightside[x]);
									bf3.append(":");
								}
							}
						}
						
						int totalsegmentsleft = 8 - totalsegments;
						
						for (int x = 0; x < totalsegmentsleft; x++) {
							bf4.append(padme);
							bf4.append(":");
						}
						
						bf2.append(bf4).append(bf3);
						myIP2 = bf2.toString().replaceAll(":$", "");
					}
				}
			}
		}
		
		String[] retarr = {myIP2, rettype};
		
		return retarr;
	}
	
	private float convertFloat(String mystr) {
		try {
			return Float.parseFloat(mystr);
		}
		catch(NumberFormatException e) {
			return 0.0F;
		}
	}
	
	private void reverse(byte[] array) {
		if (array == null) {
			return;
		}
		int i = 0;
		int j = array.length - 1;
		byte tmp;
		while (j > i) {
			tmp = array[j];
			array[j] = array[i];
			array[i] = tmp;
			j--;
			i++;
		}
	}
	
	// private byte[] readrow(final long position, final long mylen, final MappedByteBuffer mybuffer, final RandomAccessFile filehandle) throws IOException {
	private byte[] readrow(final long position, final long mylen, final ByteBuffer mybuffer, final RandomAccessFile filehandle) throws IOException {
		byte[] row = new byte[(int)mylen];
		if (UseMemoryMappedFile) {
			mybuffer.position((int)position);
			mybuffer.get(row, (int)0, (int)mylen);
		}
		else {
			filehandle.seek(position - 1);
			filehandle.read(row, (int)0, (int)mylen);
		}
		return row;
	}

	// private BigInteger read32or128(final long position, final int myiptype, final MappedByteBuffer mybuffer, final RandomAccessFile filehandle) throws IOException {
	private BigInteger read32or128(final long position, final int myiptype, final ByteBuffer mybuffer, final RandomAccessFile filehandle) throws IOException {
		if (myiptype == 4) {
			return read32(position, mybuffer, filehandle);
		}
		else if (myiptype == 6) {
			return read128(position, mybuffer, filehandle); // only IPv6 will run this
		}
		return BigInteger.ZERO;
	}
	
	// private BigInteger read128(final long position, final MappedByteBuffer mybuffer, final RandomAccessFile filehandle) throws IOException {
	private BigInteger read128(final long position, final ByteBuffer mybuffer, final RandomAccessFile filehandle) throws IOException {
		BigInteger retval = BigInteger.ZERO;
		final int bsize = 16;
		byte buf[] = new byte[bsize];
		
		if (UseMemoryMappedFile) {
			mybuffer.position((int)position);
			// for (int x = 0; x < bsize; x++) {
				// buf[x] = mybuffer.get((int)position + x); // use absolute offset to be thread-safe
			// }
			mybuffer.get(buf, (int)0, bsize);
		}
		else {
			filehandle.seek(position - 1);
			// for (int x = 0; x < bsize; x++) {
				// buf[x] = filehandle.readByte();
			// }
			filehandle.read(buf, (int)0, bsize);
		}
		reverse(buf);
		retval = new BigInteger(1, buf);
		return retval;
	}

	private BigInteger read32_row(byte[] row, final int from) throws IOException {
		// final int to = from + 4; // 4 bytes
		final int len = 4; // 4 bytes
		byte buf[] = new byte[len];
		// byte buf[] = Arrays.copyOfRange(row, from, to); // only available in JDK 1.6 onwards
		System.arraycopy(row, from, buf, (int)0, len);
		reverse(buf);
		return new BigInteger(1, buf);
	}

	// private BigInteger read32(final long position, final MappedByteBuffer mybuffer, final RandomAccessFile filehandle) throws IOException {
	private BigInteger read32(final long position, final ByteBuffer mybuffer, final RandomAccessFile filehandle) throws IOException {
		if (UseMemoryMappedFile) {
			// simulate unsigned int by using long
			return BigInteger.valueOf(mybuffer.getInt((int)position) & 0xffffffffL); // use absolute offset to be thread-safe
		}
		else {
			final int bsize = 4;
			filehandle.seek(position - 1);
			byte buf[] = new byte[bsize];
			// for (int x = 0; x < bsize; x++) {
				// buf[x] = filehandle.readByte();
			// }
			filehandle.read(buf, (int)0, bsize);
			reverse(buf);
			return new BigInteger(1, buf);
		}
	}

	// private String readStr(long position, final RandomAccessFile filehandle) throws IOException {
	private String readStr(long position, final ByteBuffer mydatabuffer, final RandomAccessFile filehandle) throws IOException {
		final int size;
		// char cbuf[] = null;
		byte[] buf = null;
		
		if (UseMemoryMappedFile) {
			position = position - _MapDataOffset; // position stored in BIN file is for full file, not just the mapped data segment, so need to minus
			size = _MapDataBuffer.get((int)position); // use absolute offset to be thread-safe (keep using the original buffer since is absolute position & just reading 1 byte)
			
			try {
				// cbuf = new char[size];
				// for (int x = 0; x < size; x++) {
					// cbuf[x] = (char)_MapDataBuffer.get((int)position + 1 + x); // use absolute offset to be thread-safe
				// }
				buf = new byte[size];
				mydatabuffer.position((int)position + 1);
				mydatabuffer.get(buf, (int)0, size);
				
			}
			catch (NegativeArraySizeException e) {
				return null;
			}
		}
		else {
			filehandle.seek(position);
			size = filehandle.read();
			try {
				// cbuf = new char[size];
				// for (int x = 0; x < size; x++) {
					// cbuf[x] = (char)filehandle.read();
				// }
				buf = new byte[size];
				filehandle.read(buf, (int)0, size);
			}
			catch (NegativeArraySizeException e) {
				return null;
			}
		}
		
		String s = new String(buf);
		return s;
		// return String.copyValueOf(cbuf);
	}

	private float readFloat_row(byte[] row, final int from) {
		// final int to = from + 4; // 4 bytes
		final int len = 4; // 4 bytes
		byte buf[] = new byte[len];
		// byte buf[] = Arrays.copyOfRange(row, from, to); // only available in JDK 1.6 onwards
		System.arraycopy(row, from, buf, (int)0, len);
		// float f = ByteBuffer.wrap(buf).order(ByteOrder.LITTLE_ENDIAN).getFloat();
		// return f;
		return Float.intBitsToFloat((buf[3]&0xff)<<24|(buf[2]&0xff)<<16|(buf[1]&0xff)<<8|(buf[0]&0xff)); // the AND is converting byte to unsigned byte in the form of an int
	}
	
	private float readFloat(final long position, final MappedByteBuffer mybuffer, final RandomAccessFile filehandle) throws IOException {
		if (UseMemoryMappedFile) {
			return mybuffer.getFloat((int)position);
		}
		else {
			final int bsize = 4;
			filehandle.seek(position - 1);
			int ptr[] = new int[bsize];
			for (int x = 0; x < bsize; x++) {
				ptr[x] = filehandle.read();
			}
			return Float.intBitsToFloat(ptr[3]<<24|ptr[2]<<16|ptr[1]<<8|ptr[0]);
		}
	}
	
	private String setDecimalPlaces(float myfloat) {
		Locale currentLocale = Locale.getDefault();
		NumberFormat nf = NumberFormat.getNumberInstance(currentLocale);
		DecimalFormat df = (DecimalFormat)nf;
		df.applyPattern("###.######");
		String fstr = df.format(myfloat).replace(',', '.');
		// System.out.println(fstr);
		return fstr;
	}
	
	private BigInteger[] ip2no(String ipstring) throws UnknownHostException {
		BigInteger a1 = BigInteger.ZERO;
		BigInteger a2 = BigInteger.ZERO;
		BigInteger a3 = new BigInteger("4");
		
		if (pattern.matcher(ipstring).matches()) { // should be IPv4
			a1 = new BigInteger("4");
			a2 = new BigInteger(String.valueOf(ipv4no(ipstring)));
		}
		else if (pattern2.matcher(ipstring).matches() || pattern3.matcher(ipstring).matches()) {
			throw new UnknownHostException();
		}
		else {
			a3 = new BigInteger("6");
			final InetAddress ia = InetAddress.getByName(ipstring);
			final byte byteArr[] = ia.getAddress();
			
			String myiptype = "0"; // BigInteger needs String in the constructor
			
			if (ia instanceof Inet6Address) {
				myiptype = "6";
			}
			else if (ia instanceof Inet4Address) { // this will run in cases of IPv4-mapped IPv6 addresses
				myiptype = "4";
			}
			a2 = new BigInteger(1, byteArr); // confirmed correct for IPv6
			
			if (a2.compareTo(FROM_6TO4) >= 0 && a2.compareTo(TO_6TO4) <= 0) {
				// 6to4 so need to remap to ipv4
				myiptype = "4";
				a2 = a2.shiftRight(80);
				a2 = a2.and(LAST_32BITS);
				a3 = new BigInteger("4");
			}
			else if (a2.compareTo(FROM_TEREDO) >= 0 && a2.compareTo(TO_TEREDO) <= 0) {
				// Teredo so need to remap to ipv4
				myiptype = "4";
				a2 = a2.not();
				a2 = a2.and(LAST_32BITS);
				a3 = new BigInteger("4");
			}
			
			a1 = new BigInteger(myiptype);
		}
		BigInteger[] bi = new BigInteger[] { a1, a2, a3 };
		
		return bi;
	}
	
	private long ipv4no(final String ipstring) {
		final String[] ipAddressInArray = ipstring.split("\\.");
		long result = 0;
		long ip = 0;
		for (int x = 3; x >= 0; x--) {
			ip = Long.parseLong(ipAddressInArray[3 - x]);
			result |= ip << (x << 3);
		}
		return result;
	}
}
