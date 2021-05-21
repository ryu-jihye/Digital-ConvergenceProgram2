package org.jihyeong.service;

import org.springframework.stereotype.Service;

@Service("sampleService")
public class SampleServiceImpl implements SampleService {
	@Override
    public Integer doAdd(String str1,String str2)throws Exception{
    	return Integer.parseInt(str1)+Integer.parseInt(str2);
    }

	@Override
	public void addData(String str) {
		// TODO Auto-generated method stub
		
	}
}
