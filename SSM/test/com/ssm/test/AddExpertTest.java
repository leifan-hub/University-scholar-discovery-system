package com.ssm.test;

import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;

import com.ssm.domain.Expert;
import com.ssm.service.ExpertService;
/**
* author����־�� 
* create: time: 2020-07-05
* update��time:  2020-07-07
*/

public class AddExpertTest extends BaseTest {
	@Autowired
    private ExpertService expertService;
	
	@Test
    public void insert() {
		Expert expert=new Expert();
		expert.setName("����");
		expert.setMajor("�����");
		expert.setSchool("�人��ѧ");
		expert.setIntroduction("���޼��");
		expert.setPaper("��������");
		expert.setResearch_direction("������");
		expert.setSubject("�������");
       int i= expertService.addExpert(expert);
      if(i==1) {System.out.println("��ӳɹ�");
    }else {
    	System.out.println("���ʧ��");}
    }



}
