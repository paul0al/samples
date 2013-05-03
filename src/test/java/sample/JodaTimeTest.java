package sample;

import org.joda.time.DateTime;
import org.joda.time.DateTimeUtils;
import org.joda.time.DateTimeZone;
import org.testng.Assert;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

public class JodaTimeTest {
	// http://www.epochconverter.com/
	private static final long JAN_01_2010_MIDNIGHT_GMT = 1262304000000L;
	private static final long JAN_01_2010_13_22_21_GMT = 1262352141000L;
	
	@BeforeTest public void setup() {
		DateTimeZone.setDefault(DateTimeZone.UTC);
	}
	
	@Test public void freezingTimeForTesting() {
		DateTimeUtils.setCurrentMillisFixed(JAN_01_2010_MIDNIGHT_GMT);

		DateTime dateTime = new DateTime();
		
		Assert.assertEquals(dateTime.getMillis(), JAN_01_2010_MIDNIGHT_GMT);
	}
	
	@Test public void truncateTime() {
		DateTimeUtils.setCurrentMillisFixed(JAN_01_2010_13_22_21_GMT);
		
		DateTime dateTime = new DateTime();
		dateTime = dateTime.withMillisOfDay(0);	// truncate the hours, minutes and seconds
		
		Assert.assertEquals(dateTime.getMillis(), JAN_01_2010_MIDNIGHT_GMT);
	}
	
	@Test public void addDays() {
		DateTimeUtils.setCurrentMillisFixed(JAN_01_2010_MIDNIGHT_GMT);
		
		DateTime dateTime = new DateTime();
		dateTime = dateTime.plusDays(5);
		
		Assert.assertEquals(dateTime.toString(), "2010-01-06T00:00:00.000Z");
	}
}
