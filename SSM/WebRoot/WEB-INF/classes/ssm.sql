-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: ssm
-- ------------------------------------------------------
-- Server version	5.7.27-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `expert`
--

DROP TABLE IF EXISTS `expert`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `expert` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) CHARACTER SET utf8 NOT NULL,
  `school` varchar(45) CHARACTER SET utf8 DEFAULT NULL,
  `major` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `subject` varchar(150) CHARACTER SET utf8 DEFAULT NULL,
  `paper` varchar(2000) CHARACTER SET utf8 DEFAULT NULL,
  `research_direction` varchar(2000) CHARACTER SET utf8 DEFAULT NULL,
  `introduction` varchar(2000) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=ujis;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expert`
--

LOCK TABLES `expert` WRITE;
/*!40000 ALTER TABLE `expert` DISABLE KEYS */;
INSERT INTO `expert` VALUES (1,'罗俊','华中科技大学','物理','引力物理','《光子静止质量实验》','地球物理','罗俊，男，汉族，1956年11月出生，湖北仙桃人。引力物理专家，博士生导师，长江特聘教授。长期从事引力实验的精密测量物理研究，开展了牛顿万有引力常数G的精确测量，实验结果被国际科技数据委员会（CODATA）基本物理常数任务组收录；开展了光子静止质量的实验检验，实验结果被国际粒子物理数据组（PDG）收录；'),(2,'吕建','南京大学','计算机','软件工程','《软件自动化》','软件自动化、面向对象语言与环境和并行程序的形式化方法','吕建教授，博士生导师，计算机软件新技术国家重点实验室主任。1960年3月生，1982年毕业于南京大学计算机系，1988年获博士学位，1993年－1994年在英国曼彻斯特大学计算机系作为访问学者。1995年在联合国大学澳门国际软件研究所从事研究工作。现任南京大学计算机科学与技术系副主任，计算机软件研究所副所长，中国计算机学会理事和江苏省计算机学会理事。'),(3,'陈文光','清华大学','计算机','计算机科学与技术','WarpLDA: a Cache Efficient O(1) Algorithm for Latent Dirichlet Allocation. ','并行处理，编程系统','我长期研究高性能计算编程模型和编译系统，近几年在以图计算系统为代表的新一代大数据处理系统方面取得了进展。'),(4,'邓志东','清华大学','计算机','计算机与自动化','A Novel Dual Successive Projection-based Model-Free Adaptive Control Method and Application to an Autonomous Car','人工智能（深度神经网络、深度强化学习），计算神经科学，无人驾驶汽车，先进机器人','我曾于1996年至1997年在香港理工大学（Hong Kong Polytechnical University）访问研究一年（对方聘用）；2001年至2003年在美国华盛顿大学（Washington University in St. Louis），以客座教授（Visiting Professor）身份工作两年（对方聘用），我曾参加美国NSF和DARPA项目的研究。'),(5,'何新贵','北京大学','计算机','计算机科学与技术','《模糊知识处理的理论与技术》#《模糊数据库系统》','人工智能（深度神经网络、深度强化学习），计算神经科学','1938年生于浙江省浦江县。1960年本科毕业于北京大学数学力学系，1967年研究生毕业于北京大学数学力学系。长期从事计算机软件和人工智能的理论研究和工程实践，提出了最优分段逼近、加权模糊逻辑、模糊分布值逻辑、可执行模糊语义网络、模糊H网、主动模糊网络、以及过程神经元网络等理念和方法，对交叉学科“知识处理学”的建立和发展起到了较大促进作用。'),(6,'孟令奎','武汉大学','遥感信息工程','摄影测量与遥感','[1].  Zushuai Wei , Yizhuo Meng , Wen Zhang , Jian Peng 和 Lingkui Meng.  Downscaling SMAP Soil Moisture Estimation with Gradient Boosting Decision Tree Regression over the Tibetan Plateau.  Remote Sensing of Environment.  225.  30-44.  2019. #\n[2].  Jueying Bai , Qian Cui , Deqing Chen , Haiwei Yu , Xudong Mao 和 Lingkui Meng.  An Approach for Downscaling SMAP Soil Moisture by Combining Sentinel-1 SAR and MODIS Data.  Remote Sensing.  10.  1302: 1-23.  2019. #\n[3].  Ziyao Li , Rui Wang , Wen Zhang , Fengmin Hu 和 Lingkui Meng.  Multiscale Features Supported DeepLabV3+ Optimization Scheme for Accurate Water Semantic Segmentation.  IEEE Access.  7.  155787-155804.  2019. #\n[4].  Lingkui Meng , Zhiyuan Zhang , Jinan Ye , Wen Zhang , Chenhan Wu 和 Chao Song.  An Automatic Extraction Method for Lakes and Reservoirs in Different Cities Using Satellite Images.  IEEE Access.  7.  62443-62456.  2019. #\n[5].  Chao Song , Cuiying Yue , Wen Zhang , Dongying Zhang , Zhiming Hong 和 Lingkui Meng.  A Remote Sensing-based Method for Drought Monitoring Using the Similarity between Drought Eigenvectors.  International Journal of Remote Sensing.  40 (23).  1-19.  2019. #\n[6].  Linyi Li , Yun Chen , Tingbao Xu , Kaifang Shi , Rui Liu , Chang Huang , Binbin Lu 和 Lingkui Meng.  Remote Sensing of Wetland Flooding at a Sub-Pixel Scale Based on Random Forests and Spatial Attraction Models.  Remote Sensing.  11.  1231,1-15.  2019. #','水利遥感监测。重点开展基于卫星遥感数据的旱情洪涝和冰凌业务化监测、应急监测、水利监管等的理论研究、工程技术及智慧水利实践。','孟令奎教授:1967年生，博士后，博士生导师，国务院特殊津贴专家，湖北省优秀研究生导师。主要研究领域:水利遥感监测、网络地理信息系统技术、计算机系统结构及高性能计算、文化地图技术与应用。1987年获河海大学学士学位，1990、1994年分别获得华中理工大学硕士和博士学位，1996年于武汉测绘科技大学测绘学博士后科研流动站出站。先后主持及参加完成了40余项国家及省部级科研计划项目和横向联合项目，在国内外重要期刊上发表学术论文180余篇，主编、合著出版教材、专著和标准6部。获国家科技进步二等奖1项，省部级一等奖和二等奖各3项。2004年被评为\"武汉大学十大杰出青年\"，同年被评为\"湖北省优秀研究生导师\"，2011年通过全校网络海选获得第二届武汉大学\"我心目中的好导师\"称号。现任全国测绘工程专业学位研究生教育协作组组长，兼任测绘遥感信息工程国家重点实验室教授。'),(7,'白征东','清华大学','土木工程系','土木工程','1.带约束的自适应抗差整体最小二乘滤波#\n\n2.Allan方差方法分析环形激光陀螺仪噪声的性能评估#\n\n3.定位测姿系统室外三维动态检定场的几何设计#\n\n4.基于距离和姿态观测量的GNSS基线网平差方法#\n\n5.一种基于CGCS2000大地线确定新方法的探讨#\n','卫星导航与定位，大地测量，工程测量','白征东，男，清华大学土木工程系地球空间信息研究所副教授。中国测绘学会工程测量分会常务理事。'),(8,'蔡宁生',' 清华大学',' 热能工程系','能源与动力工程','1.Coal-fired chemical looping combustion coupled with a high-efficiency annular carbon stripper#\n\n2.CaO carbonation kinetics determined using micro-fluidized bed thermogravimetric analysis#\n\n3.Pressurized tubular solid oxide H2O/CO2 coelectrolysis cell for direct power-to-methane#\n\n4.Measuring the fast oxidation kinetics of a manganese oxygen carrier using microfluidized bed thermogravimetric analysis#\n\n5.Hydrophobic activated carbon for elevated-temperature pressure swing adsorption#\n\n6.Simulation and energy consumption comparison of gas purification system based on elevated temperature pressure swing adsorption in ammonia synthetic system#\n\n7.基于甲烷催化部分氧化的SOFC性能研究#','洁净煤技术 二氧化碳捕集 燃料电池 煤气化联合循环发电及多联产系统','1982年毕业于西安交通大学，获得工学学士。1991年东南大学热能工程专业博士毕业，之后在东南大学热能工程研究所担任讲师，1996年获得教授职称。1999入选国家教育部\"长江学者奖励计划\"首批特聘教授2002年被聘为清华大学热能工程系教授，2004年起任热能工程系副主任，2008年起任清华大学(热能工程系)东芝能源与环境研究中心主任， 现任清华大学热能工程系学术委员会主任 。'),(9,'薛其坤','清华大学','物理学','物理','1.C. Z. Chang, J. S. Zhang, X. Feng, J. Shen, Z. C. Zhang, M. H. Guo, K. Li, Y. B. Ou, P. Wei, L. L. Wang, Z. Q. Ji, Y. Feng, S. H. Ji, X. Chen, J. F. Jia, X. Dai, Z. Fang, S. C. Zhang, K. He, Y. Y. Wang, L. Lu, X. C. Ma and Q. K. Xue, \"Experimental Observation of the Quantum Anomalous Hall Effect in a Magnetic Topological Insulator\", Science 340, 167 (2013).#\n\n2.C. L. Song, Y. L. Wang, P. Cheng, Y. P. Jiang, W. Li, T. Zhang, Z. Li, K. He, L. L. Wang, J. F. Jia, H. H. Hung, C. J. Wu, X. C. Ma, X. Chen and Q. K. Xue, \"Direct Observation of Nodes and Twofold Symmetry in FeSe Superconductor\", Science 332, 1410 (2011).#\n\n3.C. L. Song, Y. L. Wang, Y. X. Ning, J. F. Jia, X. Chen, B. Sun, P. Zhang, Q. K. Xue and X. C. Ma, \"Tailoring Phthalocyanine Metalation Reaction by Quantum Size Effect\", J. Am. Chem. Soc. 132, 1456 (2010).#\n\n4.T. Zhang, P. Cheng, W. J. Li, Y. J. Sun, G. Wang, X. G. Zhu, K. He, L. L. Wang, X. C. Ma, X. Chen, Y. Y. Wang, Y. Liu, H. Q. Lin, J. F. Jia and Q. K. Xue, \"Superconductivity in One-Atomic-Layer Metal Films Grown on Si(111)\", Nat. Phys. 6, 104 (2010).#\n\n5.P. Jiang, X. C. Ma, Y. X. Ning, C. L. Song, X. Chen, J. F. Jia and Q. K. Xue, \"Quantum Size Effect Directed Selective Self-Assembling of Cobalt Phthalocyanine on Pb(111) Thin Films\", J. Am. Chem. Soc. 130, 7790 (2008).#\n\n6.Y. S. Fu, S. H. Ji, X. Chen, X. C. Ma, R. Wu, C. C. Wang, W. H. Duan, X. H. Qiu, B. Sun, P. Zhang, J. F. Jia and Q. K. Xue, \"Manipulating the Kondo Resonance through Quantum Size Effects\", Phys. Rev. Lett. 99, 256601 (2007).#\n','扫描隧道显微学、表面物理、自旋电子学、拓扑绝缘量子态和低维超导电性等 。','薛其坤，男，汉族，1963年12月出生于山东省临沂市，博士，材料物理学家，中国科学院院士，中国科学院物理研究所研究员，清华大学教授、博士生导师，第二届高等学校科学研究优秀成果奖(科学技术)奖励委员会委员，北京邮电大学电子工程学院院长、北京量子信息科学研究院院长 。现任清华大学副校长。'),(10,'黄琳','北京大学 ',' 数学力学系','数学，力学','[1] 黄琳，郑应平，张迪，李雅普诺夫第二方法与最优控制器分析设计问题，自动化学报，1964, 2 (4): 203-218#\n\n[2] Hwang Ling, On the estimation of the decaying time, Proceeding of the 2nd congress IFAC, 576-583, 1963, Basel, Switzerland.#\n\n[3] L. Huang and C. V. Hollot, Results on positive pairs of polynomials and their application to the construction of stability domains, Int. J. Control, 1987, 46(1): 153-159#\n\n[4] A. C. Bartlett, C. V. Hollot and L. Huang, Root locations of the entire polynomials: It suffices to check the edges, Math of Control, Signals, and Systems, 1988, 1(1): 61-71#\n\n[5] Huang Lin, Chen Decheng and Luo Huageng, Approximate modeling of an elastic structure according to test date with various confidences. ACTA Mecha. Sinica, 1988, 4 (3): 248-254#\n\n[6] L. Huang and Z. Li., Fundamental theorem for optimal output feedback problem with quadratic performance criterion, Int. J. Control, 1989, 50 (6): 2341 - 2347#\n\n[7] L. Huang and L. Wang, The value mapping and parameterization approach to robust stability analysis, Science in China, 1991, 34 (10): 1222-1232#\n','系统稳定性与控制理论方面的研究工作','黄琳，控制科学专家，中国科学院院士。现为北京大学力学与工程科学系教授。黄琳主要从事系统稳定性与控制理论方面的研究。给出现代控制理论中的单输入系统极点配置定理，二次型最优控制的存在性、唯一性与线性控制律。建立输出反馈实现二次型最优控制的充要条件，指出一般情况下该问题无解。'),(11,'高敏雪 ','中国人民大学 ','经济学','数学、管理学','1. 国民经济核算与供给侧宏观经济观察[J] #2. 有关“大中小企业划分标准”的故事[J]#\n3. 三部书连缀中国政府统计百年历史[J]# 4. 投资的定义与分层是投资统计的前提[J] #5. 生态系统生产总值的内涵、核算框架与实施条件——统计视角下的设计与论证[J]#\n','经济统计','高敏雪：女，经济学博士，中国人民大学统计学院教授，中国人民大学国民经济核算研究所所长。1980-1984年，在河北大学经济学系学习，获经济学学士学位；1984-1987年，在中国人民大学统计学系学习，获经济学硕士学位；1999-2002年，在中国人民大学统计学系在职学习，获经济学博士学位。1987年起在中国人民大学统计学系任教；1994年起被聘副教授；2001年起被聘教授；2005-2006年，在国家统计局经济核算司挂职，任副司长；2006-2009年，担任统计学院副院长。'),(12,'保铮','西安电子科技大学','电信工程','数学、物理','1. 一种基于多通道复图像空间的相位误差估计方法[P]# 2. 一种基于短合成孔径的双星干涉精确定位方法[J] #3. 基于长合成孔径的辐射源成像定位算法[J] #4. 一种星载合成孔径雷达实时统一成像方法[P]#','电信技术','1953年毕业于解放军通信工程学院（现西安电子科技大学）雷达系，并留校任教至今。历任教研室副主任、系主任、副院长，1984年至1992年出任西安电子科技大学校长。1991年当选为中国科学院学部委员（院士），曾任国务院学位委员会学科评议组成员，国家自然科学基金委员会评审组成员，国家杰出青年科学基金委员会委员，陕西省科协副主席。现任雷达信号处理国家重点实验室学术委员会主任，信息产业部电子科技委员会顾问，解放军总装备部科技委员会顾问，空军科技发展与人才培养顾问。'),(13,'何友','海军工程大学 ','电信工程','信息融合理论与技术、大数据技术','[1]徐从安,熊伟,刘瑜,何友,新生目标强度未知的单量测PHD滤波器[J]电子学报. 2016# [2]徐从安,何友,夏沭涛,程俊图,董云龙,基于随机摄动再采样的粒子概率假设密度滤波器[J]电子与信息学报.2016 #','电信技术','1982年、1988年分获海军工程大学学士和硕士学位, 1997年获清华大学博士学位。曾在德国不伦瑞克工业大学·作访问学者。现为烟台海军航空工程学院院长、教授、博士生导师,海战场信息感知与融合技术军队重点实验室主任,中国航空学会信息融合分会主任委员,中国电子学会会士, IET Fellow等。2013年当选为中国工程院院士。'),(14,'吴建平',' 清华大学','计算机科学与技术 ','数学、计算机','[1]罗龙溪,吴建平.一种供水管网漏损的自动识别和位方法#[2]李丹,王松涛,吴建平,程阳.分布式机器学习的参数同步方法及装置#[3]李丹,程阳,吴建平,网络中流量动态调整方法、系统、电子设备及存储质#',' 计算机科学与技术','吴建平(1953. 10. 4- )计算机网络专家。山东荷泽人,出生于山西省太原市。现任清华大学计算机科学与技术系教授和系主任、网络科学与网络空间研究院院长、下一代互联网国家工程实验室·主任,兼任中国教育和科研计算机网CERNET专家委员会主任和网络中心主任、国家信息化专家咨询委员会委员、中国互联网协会副理事长、IEEE Fellow,曾任亚太先进网络学会APAN主席。'),(15,'方滨兴','哈尔滨工业大学','网络与信息安全','数学、计算机','[1]张伟哲,吴毓龙,关楠,方滨兴,何慧,刘川意,张宇,崔丽杰,一种多核处理器上基于划分调度的DAG实时任务间的干扰分析方法#[2]张伟哲,魏博文,方滨兴,何慧,王德胜,余翔湛,张玥,周勇林,李志刚,朱勇,崔丽杰,张羽,一种移动物联网中的高效、安全的多用户多任务卸载方法#','网络与信息安全','方滨兴(1960. 7. 17-) 。信息网络与信息安全专家。出生于黑龙江省哈尔滨市,原籍江西省万年。目前还任哈尔滨工业大学教授,国防科技大学特聘教授,中国科学院计算技术研究所客座研究员,清华大学兼职教授。');
/*!40000 ALTER TABLE `expert` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'ssm'
--

--
-- Dumping routines for database 'ssm'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-12  8:39:57
