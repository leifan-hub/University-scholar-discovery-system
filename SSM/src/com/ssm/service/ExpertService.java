package com.ssm.service;

import java.util.List;

import com.ssm.domain.Expert;

public interface ExpertService {

	public List<Expert> getExpertList();
	public List<Expert> getExpertByName(String name);
	public Expert getExpertById(int id);
	public int addExpert(Expert expert);
	public int delete(int userId);
	public int update(Expert expert);
}
