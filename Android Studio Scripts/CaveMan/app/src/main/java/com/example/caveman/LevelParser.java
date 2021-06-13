// This java code takes the XML files that hold the description of where the enemies should appear and
// what type should they be and constructs Lists with that data.

package com.example.caveman;

import android.content.Context;

import org.xmlpull.v1.XmlPullParser;

import java.util.ArrayList;
import java.util.List;

public class LevelParser {
	private int level;// variable to store the level to be parsed
	private Context context;// The GameActivity Context
	private int resId = R.xml.level1;// The ID of the XML file to be parsed. Default is the 1st level
	private List<String> lvlStruct;// A list to hold the data extracted from the XML file
	private final int TOTALLVLS = 6;// The number of levels that the game has

	public LevelParser(Context context) {
		this.context = context;
		// ArrayList that will hold the level structure.
		lvlStruct = new ArrayList<String>();
	}

	// Returns the current level
	public int getLevel() {
		return level;
	}

	// Returns true if the current level's number is smaller than the number of the greatest level.
	public boolean hasNext(int currentLvl) {
		if (currentLvl < TOTALLVLS)
			return true;
		else
			return false;
	}

	// By using an XmlPullParser, this method extracts data from the XML files with the level structure,
	// according to their XML tags and stores that data in a List.
	public List<String> parser(int level) {
		this.level = level;
		resId = context.getResources().getIdentifier("level" + level, "xml",
				context.getPackageName());
		XmlPullParser parser = context.getResources().getXml(resId);
		try {
			while (parser.next() != XmlPullParser.END_DOCUMENT) {
				String name = parser.getName();
				String type = null;
				String time = null;
				String position = null;
				if ((name != null) && name.equals("enemy")) {
					int size = parser.getAttributeCount();
					for (int i = 0; i < size; i++) {
						String attributeN = parser.getAttributeName(i);
						String attributeV = parser.getAttributeValue(i);
						if ((attributeN != null) && attributeN.equals("type")) {
							type = attributeV;
						} else if ((attributeN != null)
								&& attributeN.equals("time")) {
							time = attributeV;
						} else if ((attributeN != null)
								&& attributeN.equals("position")) {
							position = attributeV;
						}
					}
					if ((type != null) && (time != null) && (position != null)) {
						lvlStruct.add(type);
						lvlStruct.add(time);
						lvlStruct.add(position);
					}
				}
			}
		} catch (Exception e) {
		}
		return lvlStruct;
	}
}