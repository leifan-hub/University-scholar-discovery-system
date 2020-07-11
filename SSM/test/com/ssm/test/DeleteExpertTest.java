package com.ssm.test;



import java.util.List;

import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;

import com.ssm.domain.Expert;
import com.ssm.service.ExpertService;


public class DeleteExpertTest extends BaseTest {
	@Autowired
    private ExpertService expertService;
	
	@Test
    public void delete() {
		
	int i=	expertService.delete(3);
		if(i==1) {System.out.println("É¾³ý³É¹¦");}
		else {
			System.out.println("É¾³ýÊ§°Ü");
		}
		
	}


}