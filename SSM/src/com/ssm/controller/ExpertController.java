package com.ssm.controller;
import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

import com.ssm.domain.Countclass;
import com.ssm.domain.Expert;
import com.ssm.service.ExpertService;
/**
* author£ººúÖ¾ºÀ ÀîÁú¾ü À×·² Í¿çìçâ
* create: time: 2020-07-05
* update£ºtime:  2020-07-12
*/
@Controller
@RequestMapping("expert")
public class ExpertController {

	@Autowired
	private ExpertService expertService;
	
//	@RequestMapping("/getExpertList")
//	public ModelAndView getUserList() {
//		List<Expert> expertList = expertService.getExpertList();
//		
//		ModelAndView model = new ModelAndView();
//		model.addObject("expertList", expertList);
//		model.setViewName("expertDetail");
//		return model;
//	}
	
	
	@ResponseBody
	@RequestMapping("/getJson")
	public List<Countclass> getJson(ModelAndView model) {
		System.out.println("º¯ÊýÖ´ÐÐ");
		List<Countclass> countnums = expertService.countnums();
		for(Countclass n:countnums) {
			System.out.println(n.getName());
			System.out.println(n.getNum());
		}
		model.addObject("countnums", countnums);
		
		return countnums;
	}
	
	
	
	@RequestMapping("/returnIndex")
	public ModelAndView returnIndex() {
		List<Expert> expertList = expertService.getExpertList();
		List<List<String>> expertR_D = new ArrayList<List<String>>();
		List<String> expertPic = new ArrayList<String>();
		for(Expert expert : expertList) {
			List<String>expertDirections=new ArrayList<String>();
			String picUrl =expertService.getExpertPicByName(expert.getName());
						
			String[] expertDirections_string=expert.getResearch_direction().split(",|¡£|¡¢");
			for (String expertDirection : expertDirections_string) {
				expertDirections.add(expertDirection);
			}
			expertR_D.add(expertDirections);
			expertPic.add(picUrl);
		}
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expertList);
		model.addObject("expertR_D", expertR_D);
		model.addObject("expertPic", expertPic);
		model.setViewName("index");
		return model;		
	}
	
	@RequestMapping("/getExpertByName")
	public ModelAndView getExpertByName(String name) {
		List<Expert> expertList = expertService.getExpertByName(name);
		List<List<String>> expertR_D = new ArrayList<List<String>>();
		List<String> expertPic = new ArrayList<String>();
		for(Expert expert : expertList) {
			List<String>expertDirections=new ArrayList<String>();
			String picUrl =expertService.getExpertPicByName(expert.getName());
						
			String[] expertDirections_string=expert.getResearch_direction().split(",|¡£|¡¢");
			for (String expertDirection : expertDirections_string) {
				expertDirections.add(expertDirection);
			}
			expertR_D.add(expertDirections);
			expertPic.add(picUrl);
		}
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expertList);
		model.addObject("expertR_D", expertR_D);
		model.addObject("expertPic", expertPic);
		model.setViewName("queryExpertName");
		return model;
	}
	
	@RequestMapping("/getExpertBySchool")
	public ModelAndView getExpertBySchool(String school) {
		List<Expert> expertList = expertService.getExpertBySchool(school);
		List<List<String>> expertR_D = new ArrayList<List<String>>();
		List<String> expertPic = new ArrayList<String>();
		for(Expert expert : expertList) {
			List<String>expertDirections=new ArrayList<String>();
			String picUrl =expertService.getExpertPicByName(expert.getName());
						
			String[] expertDirections_string=expert.getResearch_direction().split(",|¡£|¡¢");
			for (String expertDirection : expertDirections_string) {
				expertDirections.add(expertDirection);
			}
			expertR_D.add(expertDirections);
			expertPic.add(picUrl);
		}
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expertList);
		model.addObject("expertR_D", expertR_D);
		model.addObject("expertPic", expertPic);
		model.setViewName("queryExpertSchool");
		return model;
	}
	
	@RequestMapping("/getExpertByMajor")
	public ModelAndView getExpertByMajor(String major) {
		List<Expert> expertList = expertService.getExpertByMajor(major);
		List<List<String>> expertR_D = new ArrayList<List<String>>();
		List<String> expertPic = new ArrayList<String>();
		for(Expert expert : expertList) {
			List<String>expertDirections=new ArrayList<String>();
			String picUrl =expertService.getExpertPicByName(expert.getName());
						
			String[] expertDirections_string=expert.getResearch_direction().split(",|¡£|¡¢");
			for (String expertDirection : expertDirections_string) {
				expertDirections.add(expertDirection);
			}
			expertR_D.add(expertDirections);
			expertPic.add(picUrl);
		}
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expertList);
		model.addObject("expertR_D", expertR_D);
		model.addObject("expertPic", expertPic);
		model.setViewName("queryExpertMajor");
		return model;
	}	
	
	@RequestMapping("/getExpertBySubject")
	public ModelAndView getExpertBySubject(String subject) {
		List<Expert> expertList = expertService.getExpertBySubject(subject);
		List<List<String>> expertR_D = new ArrayList<List<String>>();
		List<String> expertPic = new ArrayList<String>();
		for(Expert expert : expertList) {
			List<String>expertDirections=new ArrayList<String>();
			String picUrl =expertService.getExpertPicByName(expert.getName());
						
			String[] expertDirections_string=expert.getResearch_direction().split(",|¡£|¡¢");
			for (String expertDirection : expertDirections_string) {
				expertDirections.add(expertDirection);
			}
			expertR_D.add(expertDirections);
			expertPic.add(picUrl);
		}
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expertList);
		model.addObject("expertR_D", expertR_D);
		model.addObject("expertPic", expertPic);
		model.setViewName("queryExpertSubject");
		return model;
	}	
	
	@RequestMapping("/getExpertByPaper")
	public ModelAndView getExpertByPaper(String paper) {
		List<Expert> expertList = expertService.getExpertByPaper(paper);
		List<List<String>> expertR_D = new ArrayList<List<String>>();
		List<String> expertPic = new ArrayList<String>();
		for(Expert expert : expertList) {
			List<String>expertDirections=new ArrayList<String>();
			String picUrl =expertService.getExpertPicByName(expert.getName());
						
			String[] expertDirections_string=expert.getResearch_direction().split(",|¡£|¡¢");
			for (String expertDirection : expertDirections_string) {
				expertDirections.add(expertDirection);
			}
			expertR_D.add(expertDirections);
			expertPic.add(picUrl);
		}
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expertList);
		model.addObject("expertR_D", expertR_D);
		model.addObject("expertPic", expertPic);
		model.setViewName("queryExpertPaper");
		return model;
	}	
	
	@RequestMapping("/getExpertByResearchDirection")
	public ModelAndView getExpertByResearch(String research_direction) {
		List<Expert> expertList = expertService.getExpertByResearch(research_direction);
		List<List<String>> expertR_D = new ArrayList<List<String>>();
		List<String> expertPic = new ArrayList<String>();
		for(Expert expert : expertList) {
			List<String>expertDirections=new ArrayList<String>();
			String picUrl =expertService.getExpertPicByName(expert.getName());
						
			String[] expertDirections_string=expert.getResearch_direction().split(",|¡£|¡¢");
			for (String expertDirection : expertDirections_string) {
				expertDirections.add(expertDirection);
			}
			expertR_D.add(expertDirections);
			expertPic.add(picUrl);
		}
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expertList);
		model.addObject("expertR_D", expertR_D);
		model.addObject("expertPic", expertPic);
		model.setViewName("queryExpertDirection");
		return model;
	}	
	
	//@RequestMapping("/getExpertByIntroduction")
	//public ModelAndView getExpertByIntroduction(String introduction) {
	//	List<Expert> expert =expertService.getExpertByIntroduction(introduction);
		
	//	ModelAndView model = new ModelAndView();
	//	model.addObject("expertList", expert);
	//	model.setViewName("expertDetail");
	//	return model;
//	}	

	@RequestMapping("/getExpertById")
	public ModelAndView getExpertById(int id) {
		Expert expert =expertService.getExpertById(id);
		expertService.addpageview(id);
		List<String>expertPapers=new ArrayList<String>();
		List<String>expertTags=new ArrayList<String>();
		List<Expert> expertRelated =new ArrayList<Expert>();
		
		//System.out.println(expert.getName());
		String picUrl =expertService.getExpertPicByName(expert.getName());
		String[] expertPapers_string=expert.getPaper().split("#");
		for (String expertPaper : expertPapers_string) {
			expertPapers.add(expertPaper);
		}
		
		String[] expertTags_string=expertService.getExpertTagByName(expert.getName()).split("#");
		for (String expertTag : expertTags_string) {
			expertTags.add(expertTag);
		}
		List<Expert> experts =expertService.getExpertList();
		for(Expert expertTemp : experts) {   
			System.out.println(expertService.getExpertTagByName(expertTemp.getName()));
			System.out.println(expertService.getExpertTagByName(expert.getName()));
			double result=expertService.getSimilarity(expertService.getExpertTagByName(expertTemp.getName()),expertService.getExpertTagByName(expert.getName()));
			if(result>0.35&&!(expertTemp.getName().equals(expert.getName()))) {
				expertTemp.setMajor(expertService.getExpertPicByName(expertTemp.getName()));;
				expertRelated.add(expertTemp);
			}
		}     
		ModelAndView model = new ModelAndView();
		model.addObject("expert", expert);
		model.addObject("expertRelated", expertRelated);
		model.addObject("expertPapers", expertPapers);
		model.addObject("expertTags", expertTags);
		model.addObject("picUrl", picUrl);
		model.setViewName("expertDetail");
		return model;
	}	
	
	
}