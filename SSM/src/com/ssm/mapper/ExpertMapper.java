package com.ssm.mapper;

import java.util.List;
import com.ssm.domain.Expert;


public interface ExpertMapper {
	public List<Expert> getExpertList();
	public List<Expert> getExpertByName(String name);
	public Expert getExpertById(int id);
	public int addExpert(Expert expert);
	public int delete(int id);
	public int update(Expert expert);
}
