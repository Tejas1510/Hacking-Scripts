package com.ip2location;

import java.util.regex.*;
import java.net.URL;
import java.net.URLEncoder;
import java.lang.StringBuffer; 
import com.google.gson.*;
import org.apache.commons.lang3.StringUtils;


public class IP2LocationWebService {
	private static final Pattern pattern = Pattern.compile("^[\\dA-Z]{10}$");
	private static final Pattern pattern2 = Pattern.compile("^WS\\d+$");
	
	private String _APIKey = "";
	private String _Package = "";
	private boolean _UseSSL = true;

	public IP2LocationWebService() {
	
	}
	
	/**
	* This function initializes the params for the web service.
	*/
	public void Open(String APIKey, String Package) throws IllegalArgumentException {
		Open(APIKey, Package, true);
	}
	
	/**
	* This function initializes the params for the web service.
	*/
	public void Open(String APIKey, String Package, boolean UseSSL) throws IllegalArgumentException {
		_APIKey = APIKey;
		_Package = Package;
		_UseSSL = UseSSL;
		
		CheckParams();
	}
	
	/**
	* This function validates the API key and package params.
	*/
	private void CheckParams() throws IllegalArgumentException {
		if ((!pattern.matcher(_APIKey).matches()) && (!_APIKey.equals("demo"))) {
			throw new IllegalArgumentException("Invalid API key.");
		}
		else if (!pattern2.matcher(_Package).matches()) {
			throw new IllegalArgumentException("Invalid package name.");
		}
	}
	

	public JsonObject IPQuery(String IPAddress) throws IllegalArgumentException, RuntimeException {
		return IPQuery(IPAddress, null, "en");
	}

	public JsonObject IPQuery(String IPAddress, String Language) throws IllegalArgumentException, RuntimeException {
		return IPQuery(IPAddress, null, Language);
	}
	

	public JsonObject IPQuery(String IPAddress, String[] AddOns, String Language) throws IllegalArgumentException, RuntimeException {
		try {
			String myurl;
			String myjson;
			CheckParams(); // check here in case user haven't called Open yet
			
			StringBuffer bf = new StringBuffer();
			bf.append("http");
			if (_UseSSL) {
				bf.append("s");
			}
			bf.append("://api.ip2location.com/v2/?key=").append(_APIKey).append("&package=").append(_Package).append("&ip=").append(URLEncoder.encode(IPAddress, "UTF-8")).append("&lang=").append(URLEncoder.encode(Language, "UTF-8"));
			
			if ((AddOns != null) && (AddOns.length > 0)) {
				bf.append("&addon=").append(URLEncoder.encode(StringUtils.join(AddOns, ","), "UTF-8"));
			}
			myurl = bf.toString();
			
			myjson = Http.get(new URL(myurl));
			
			JsonParser parser = new JsonParser();
			JsonObject myresult = parser.parse(myjson).getAsJsonObject();
			return myresult;
		}
		catch (IllegalArgumentException ex) {
			throw ex;
		}
		catch (Exception ex2) {
			throw new RuntimeException(ex2);
		}
	}
	

	public JsonObject GetCredit() throws IllegalArgumentException, RuntimeException {
		try {
			String myurl;
			String myjson;
			CheckParams(); // check here in case user haven't called Open yet
			
			StringBuffer bf = new StringBuffer();
			bf.append("http");
			if (_UseSSL) {
				bf.append("s");
			}
			bf.append("://api.ip2location.com/v2/?key=").append(_APIKey).append("&check=true");
			
			myurl = bf.toString();
			
			myjson = Http.get(new URL(myurl));
			
			JsonParser parser = new JsonParser();
			JsonObject myresult = parser.parse(myjson).getAsJsonObject();
			return myresult;
		}
		catch (IllegalArgumentException ex) {
			throw ex;
		}
		catch (Exception ex2) {
			throw new RuntimeException(ex2);
		}
	}
}