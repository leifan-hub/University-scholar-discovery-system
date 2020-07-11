package com.ssm.test;



import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;

import com.ssm.domain.Expert;
import com.ssm.service.ExpertService;


public class UpdateExpertTest extends BaseTest {
	@Autowired
    private ExpertService expertService;
	
	@Test
    public void update() {
		Expert expert=new Expert();
		expert.setId(1);
		expert.setName("李四光");
		expert.setMajor("计算机科学与技术");
		expert.setSchool("武汉大学");
		expert.setIntruduction("暂无简介");
		expert.setPaper("暂无论文");
		expert.setResearch_direction("数据挖掘与数据分析");
		expert.setSubject("软件工程");
       int i= expertService.update(expert);
      if(i==1) {System.out.println("更新成功");
    }else {
    	System.out.println("更新失败");}
    }



}