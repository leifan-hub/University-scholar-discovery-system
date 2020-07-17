package com.ssm.test;

import static org.junit.Assert.*;

import java.util.List;

import org.junit.Before;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.util.Assert;
import com.ssm.domain.Expert;
import com.ssm.service.ExpertService;

public class ExpertControllerTest extends BaseTest {

	@Autowired
	private ExpertService expertService;
	@Before
	public void setUp() throws Exception {
	}

	@Test
	public void testGetExpertByName() {
		String name="薛其坤";
		List<Expert> expertList =expertService.getExpertByName(name);
		for(Expert expert : expertList) {
			Assert.isTrue(expert.getName().contains(name));
		}
	}

	@Test
	public void testGetExpertBySchool() {
		String school="清华大学";
		List<Expert> expertList =expertService.getExpertBySchool(school);
		for(Expert expert : expertList) {
			Assert.isTrue(expert.getSchool().contains(school));
		}
	}

	@Test
	public void testGetExpertByMajor() {
		String major="物理";
		List<Expert> expertList =expertService.getExpertByMajor(major);
		for(Expert expert : expertList) {
			Assert.isTrue(expert.getMajor().contains(major));
		}
	}

	@Test
	public void testGetExpertBySubject() {
		String subject="物理";
		List<Expert> expertList =expertService.getExpertBySubject(subject);
		for(Expert expert : expertList) {
			Assert.isTrue(expert.getSubject().contains(subject));
		}
	}

	@Test
	public void testGetExpertByPaper() {
		String paper="《光子静止质量实验》";
		List<Expert> expertList =expertService.getExpertByPaper(paper);
		for(Expert expert : expertList) {
			Assert.isTrue(expert.getPaper().contains(paper));
		}
	}

	@Test
	public void testGetExpertByResearch() {
		String re="电信技术";
		List<Expert> expertList =expertService.getExpertByResearch(re);
		for(Expert expert : expertList) {
			Assert.isTrue(expert.getResearch_direction().contains(re));
		}
	}

	@Test
	public void testGetExpertById() {
		Expert expert =expertService.getExpertById(5);
		assertEquals(5,expert.getId());
	}

}
