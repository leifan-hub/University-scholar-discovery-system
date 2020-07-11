package com.ssm.test;



import java.util.List;

import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;

import com.ssm.domain.Expert;
import com.ssm.service.ExpertService;


public class SearchExpertTest extends BaseTest {
	@Autowired
    private ExpertService expertService;
	
	@Test
    public void search() {
		
		List<Expert> expertList = expertService.getExpertList();
		for(Expert expert : expertList) {
			
		System.out.println(expert.getName()+"  "+expert.getMajor()+"  "+expert.getSchool()+"  "+expert.getSubject()+"  "+expert.getIntroduction());
		}
		
		
		
	}


}