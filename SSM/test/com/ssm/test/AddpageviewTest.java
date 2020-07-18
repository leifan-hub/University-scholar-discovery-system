package com.ssm.test;

import org.junit.Assert;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;

import com.ssm.domain.Expert;
import com.ssm.service.ExpertService;
/**
* author£ººúÖ¾ºÀ 
* create: time: 2020-07-16
* update£ºtime:  2020-07-16
*/

public class AddpageviewTest extends BaseTest {
	@Autowired
    private ExpertService expertService;
	
	@Test
    public void addpageview() {
		
      Expert  expert=expertService.getExpertById(1);
      int pageview1=expert.getPageview();
      System.out.println(pageview1);
      expertService.addpageview(1);
   Expert   expert2=expertService.getExpertById(1);
      int pageview2=expert2.getPageview();
      System.out.println(pageview2);
      Assert.assertEquals(pageview1+1, pageview2);
    }



}