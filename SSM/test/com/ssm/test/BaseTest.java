package com.ssm.test;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.test.context.web.WebAppConfiguration;
 

@RunWith(SpringJUnit4ClassRunner.class)
@WebAppConfiguration("config")
@ContextConfiguration(locations = { "classpath:spring/springmvc.xml", "classpath:spring/applicationContext-dao.xml","classpath:spring/applicationContext-service.xml","classpath:mybatis/mybatisConfig.xml" })
public class BaseTest {
 
    @Test
    public void test() {
    }
}
