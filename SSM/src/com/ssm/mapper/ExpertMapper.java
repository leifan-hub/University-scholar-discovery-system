package com.ssm.mapper;

import java.util.List;

import org.springframework.web.servlet.ModelAndView;

import com.ssm.domain.Expert;


public interface ExpertMapper {
	public List<Expert> getExpertList();
	public List<Expert> getExpertByName(String name);
	public List<Expert> getExpertBySchool(String school);
	public List<Expert> getExpertByMajor(String major);
	public List<Expert> getExpertBySubject(String subject);
	public List<Expert> getExpertByPaper(String paper);
	public List<Expert> getExpertByResearch(String research_direction);
	public List<Expert> getExpertByIntroduction(String introduction);
	public Expert getExpertById(int id);
	public int addExpert(Expert expert);
	public int delete(int id);
	public int update(Expert expert);
}
