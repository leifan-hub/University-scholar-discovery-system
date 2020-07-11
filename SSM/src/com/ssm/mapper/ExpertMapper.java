package com.ssm.mapper;

import java.util.List;
import com.ssm.domain.Expert;


public interface ExpertMapper {
	public List<Expert> getExpertList();
	public List<Expert> getExpertByName(String name);
	public List<Expert> getExpertBySchool(String school);
	public List<Expert> getExpertByMajor(String major);
	public List<Expert> getExpertBySubject(String subject);
	public List<Expert> getExpertByPaper(String paper);
	public List<Expert> getExpertByResearchDirection(String research_direction);
	public Expert getExpertById(int id);
	public int addExpert(Expert expert);
	public int delete(int id);
	public int update(Expert expert);
}
