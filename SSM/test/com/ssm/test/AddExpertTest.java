package com.ssm.test;

import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;

import com.ssm.domain.Expert;
import com.ssm.service.ExpertService;
/**
* author：胡志豪 
* create: time: 2020-07-05
* update：time:  2020-07-07
*/

public class AddExpertTest extends BaseTest {
	@Autowired
    private ExpertService expertService;
	
	@Test
    public void insert() {
		Expert expert=new Expert();
		expert.setName("李四");
		expert.setMajor("计算机");
		expert.setSchool("武汉大学");
		expert.setIntroduction("暂无简介");
		expert.setPaper("暂无论文");
		expert.setResearch_direction("大数据");
		expert.setSubject("软件工程");
       int i= expertService.addExpert(expert);
      if(i==1) {System.out.println("添加成功");
    }else {
    	System.out.println("添加失败");}
    }



}
