-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        8.0.17 - MySQL Community Server - GPL
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  10.3.0.5771
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- sitedb 데이터베이스 구조 내보내기
DROP DATABASE IF EXISTS `sitedb`;
CREATE DATABASE IF NOT EXISTS `sitedb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `sitedb`;

-- 테이블 sitedb.board 구조 내보내기
DROP TABLE IF EXISTS `board`;
CREATE TABLE IF NOT EXISTS `board` (
  `bid` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) DEFAULT NULL,
  `bpass` varchar(45) DEFAULT NULL,
  `content` text,
  `createdate` varchar(45) DEFAULT NULL,
  `updatedate` varchar(45) DEFAULT NULL,
  `uid` varchar(10) DEFAULT NULL,
  `viewcount` int(11) DEFAULT NULL,
  `replycount` int(11) DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  PRIMARY KEY (`bid`),
  KEY `fk_board_user_idx` (`uid`),
  KEY `fk_board_category_idx` (`cid`),
  CONSTRAINT `fk_board_category` FOREIGN KEY (`cid`) REFERENCES `category` (`cid`),
  CONSTRAINT `fk_board_user` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 sitedb.category 구조 내보내기
DROP TABLE IF EXISTS `category`;
CREATE TABLE IF NOT EXISTS `category` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `cname` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 sitedb.reply 구조 내보내기
DROP TABLE IF EXISTS `reply`;
CREATE TABLE IF NOT EXISTS `reply` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `rcontent` text,
  `bid` int(11) DEFAULT NULL,
  `createdate` varchar(45) DEFAULT NULL,
  `updatedate` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`rid`),
  KEY `fk_reply_board_idx` (`bid`),
  CONSTRAINT `fk_reply_board` FOREIGN KEY (`bid`) REFERENCES `board` (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 sitedb.user 구조 내보내기
DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `uid` varchar(10) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `pass` varchar(45) DEFAULT NULL,
  `grade` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
