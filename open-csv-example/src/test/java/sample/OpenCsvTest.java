package sample;

import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Arrays;

import org.apache.commons.io.IOUtils;
import org.testng.annotations.Test;

import au.com.bytecode.opencsv.CSVReader;

public class OpenCsvTest {

	/**
	 * Example that parse csv files that escapes column values containing new line, double quotes and commas.
	 * as specified by http://tools.ietf.org/html/rfc4180. 
	 * @throws Exception
	 */
    @Test public void readCsvFile() throws Exception {
        InputStream in = this.getClass().getClassLoader().getResourceAsStream("file.csv");
        CSVReader reader = new CSVReader(new InputStreamReader(in));
        
        String [] line = null;
        
        try {
	        while ((line = reader.readNext()) != null) {
	            System.out.println(Arrays.toString(line));
	        }
        } finally {
        	IOUtils.closeQuietly(in);
        }
    }
}
