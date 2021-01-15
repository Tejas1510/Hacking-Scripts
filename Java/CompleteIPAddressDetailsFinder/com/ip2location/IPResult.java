package com.ip2location;

/**
* This class is used to store the geolocation data that is returned by the IP2Location class.
* <p>
* <b>Requirements:</b> Java SDK 1.4 or later<br>
* <p>
* Copyright (c) 2002-2020 IP2Location.com
* <p>
*
* @author IP2Location.com
* @version 8.5.0
*/
public class IPResult {
	static final String NOT_SUPPORTED = "Not_Supported";
	String ip_address;
	String country_short;
	String country_long;
	String region;
	String city;
	String isp;
	float latitude;
	float longitude;
	String domain;
	String zipcode;
	String netspeed;
	String timezone;
	String iddcode;
	String areacode;
	String weatherstationcode;
	String weatherstationname;
	String mcc;
	String mnc;
	String mobilebrand;
	float elevation;
	String usagetype;
	String status;
	boolean delay=false;
	String version = "Version 8.5.0";
	IPResult(String ipstring) {
		ip_address = ipstring;
	}
/**
 * This method to get two-character country code based on ISO 3166.
 * @return the country code
 */
	public String getCountryShort() { return country_short; }
/**
 * This method to get country name based on ISO 3166.
 * @return the country name.
 */
	public String getCountryLong() { return country_long; }
/**
 * This method to get region or state name.
 * @return the region or state name.
 */
	public String getRegion() { return region; }
/**
 * This method to get city name.
 * @return the city name.
 */
	public String getCity() { return city; }
/**
 * This method to get Internet Service Provider (ISP) name.
 * @return the ISP name.
 */
	public String getISP() { return isp; }
/**
 * This method to get city latitude.
 * @return the city latitude.
 */
	public float getLatitude() { return latitude; }
/**
 * This method to get city longitude.
 * @return the city longitude.
 */
	public float getLongitude() { return longitude; }
/**
 * This method to get IP internet domain name associated to IP address range.
 * @return the domain name.
 */
	public String getDomain() { return domain; }
/**
 * This method to get ZIP/Postal code.
 * @return the ZIP/Postal code.
 */
	public String getZipCode() { return zipcode; }
/**
 * This method to get UTC time zone.
 * @return the time zone.
 */
	public String getTimeZone() { return timezone; }
/**
 * This method to get internet connection speed (DIAL) DIAL-UP,(DSL) DSL/CABLE or(COMP) COMPANY
 * @return the net speed
 */
	public String getNetSpeed() { return netspeed; }
/**
 * This method to get the IDD prefix to call the city from another country.
 * @return the idd code
 */
	public String getIDDCode() { return iddcode; }
/**
 * This method to get the varying length number assigned to geographic areas for call between cities.
 * @return the area code
 */
	public String getAreaCode() { return areacode; }
/**
 * This method to get the special code to identify the nearest weather observation station.
 * @return the weather station code
 */
	public String getWeatherStationCode() { return weatherstationcode; }
/**
 * This method to get the name of the nearest weather observation station.
 * @return the weather station name
 */
	public String getWeatherStationName() { return weatherstationname; }
/**
 * This method to get the mobile country code.
 * @return the mobile country code
 */
	public String getMCC() { return mcc; }
/**
 * This method to get the mobile network code.
 * @return the mobile network code
 */
	public String getMNC() { return mnc; }
/**
 * This method to get the mobile brand.
 * @return the mobile brand
 */
	public String getMobileBrand() { return mobilebrand; }
/**
 * This method to get city elevation.
 * @return the city elevation.
 */
	public float getElevation() { return elevation; }
/**
 * This method to get usage type.
 * @return the usage type.
 */
	public String getUsageType() { return usagetype; }
/**
 * This method to get status code of query.
 * @return the status code
 */
	public String getStatus() { return status; }
/**
 * This method to get component delay.
 * @return the component delay.
 */
	public boolean getDelay() { return delay; }
/**
 * This method to get component version.
 * @return the component version.
 */
	public String getVersion() { return version; }
/**
 * This method to return all the fields.
 * @return the result in a formatted string.
 */
	public String toString() {
		String NL = System.getProperty("line.separator");
		StringBuffer buf = new StringBuffer("IP2LocationRecord:"+NL);
		buf.append("\tIP Address = "+ip_address+NL);
		buf.append("\tCountry Short = "+country_short+NL);
		buf.append("\tCountry Long = "+country_long+NL);
		buf.append("\tRegion = "+region+NL);
		buf.append("\tCity = "+city+NL);
		buf.append("\tISP = "+isp+NL);
		buf.append("\tLatitude = "+latitude+NL);
		buf.append("\tLongitude = "+longitude+NL);
		buf.append("\tDomain = "+domain+NL);
		buf.append("\tZipCode = "+zipcode+NL);
		buf.append("\tTimeZone = "+timezone+NL);
		buf.append("\tNetSpeed = "+netspeed+NL);
		buf.append("\tIDDCode = "+iddcode+NL);
		buf.append("\tAreaCode = "+areacode+NL);
		buf.append("\tWeatherStationCode = "+weatherstationcode+NL);
		buf.append("\tWeatherStationName = "+weatherstationname+NL);
		buf.append("\tMCC = "+mcc+NL);
		buf.append("\tMNC = "+mnc+NL);
		buf.append("\tMobileBrand = "+mobilebrand+NL);
		buf.append("\tElevation = "+elevation+NL);
		buf.append("\tUsageType = "+usagetype+NL);
		return buf.toString();
	}
}
