package com.ip2location;

// package-private access
class MetaData {
	private int _BaseAddr = 0;
	private int _DBCount = 0;
	private int _DBColumn = 0;
	private int _DBType = 0;
	private int _DBDay = 1;
	private int _DBMonth = 1;
	private int _DBYear = 1;
	private int _BaseAddrIPv6 = 0;
	private int _DBCountIPv6 = 0;
	private boolean _OldBIN = false;
	private boolean _Indexed  = false;
	private boolean _IndexedIPv6 = false;
	private int _IndexBaseAddr = 0;
	private int _IndexBaseAddrIPv6 = 0;
	
	MetaData() {
	
	}
	
	// all package-private access
	int getBaseAddr() { return _BaseAddr; }
	int getDBCount() { return _DBCount; }
	int getDBColumn() { return _DBColumn; }
	int getDBType() { return _DBType; }
	int getDBDay() { return _DBDay; }
	int getDBMonth() { return _DBMonth; }
	int getDBYear() { return _DBYear; }
	int getBaseAddrIPv6() { return _BaseAddrIPv6; }
	int getDBCountIPv6() { return _DBCountIPv6; }
	boolean getOldBIN() { return _OldBIN; }
	boolean getIndexed() { return _Indexed; }
	boolean getIndexedIPv6() { return _IndexedIPv6; }
	int getIndexBaseAddr() { return _IndexBaseAddr; }
	int getIndexBaseAddrIPv6() { return _IndexBaseAddrIPv6; }
	
	void setBaseAddr(int value) { _BaseAddr = value; }
	void setDBCount(int value) { _DBCount = value; }
	void setDBColumn(int value) { _DBColumn = value; }
	void setDBType(int value) { _DBType = value; }
	void setDBDay(int value) { _DBDay = value; }
	void setDBMonth(int value) { _DBMonth = value; }
	void setDBYear(int value) { _DBYear = value; }
	void setBaseAddrIPv6(int value) { _BaseAddrIPv6 = value; }
	void setDBCountIPv6(int value) { _DBCountIPv6 = value; }
	void setOldBIN(boolean value) { _OldBIN = value; }
	void setIndexed(boolean value) { _Indexed = value; }
	void setIndexedIPv6(boolean value) { _IndexedIPv6 = value; }
	void setIndexBaseAddr(int value) { _IndexBaseAddr = value; }
	void setIndexBaseAddrIPv6(int value) { _IndexBaseAddrIPv6 = value; }
}
