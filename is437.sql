-- phpMyAdmin SQL Dump
-- version 4.0.10deb1ubuntu0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 23, 2020 at 09:26 AM
-- Server version: 5.5.62-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `is437`
--

-- --------------------------------------------------------

--
-- Table structure for table `conlontj_attends`
--

CREATE TABLE IF NOT EXISTS `conlontj_attends` (
  `aid` int(4) NOT NULL AUTO_INCREMENT,
  `event_id` int(4) NOT NULL,
  `customer_id` int(4) NOT NULL,
  `review` varchar(100) NOT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `conlontj_attends`
--

INSERT INTO `conlontj_attends` (`aid`, `event_id`, `customer_id`, `review`) VALUES
(1, 2, 3, 'More hot dogs...'),
(2, 2, 3, 'More hot dogs...'),
(3, 1, 3, 'Tom'' review of "End of social distancing party": It was later than expected.'),
(4, 2, 3, 'Tom''s review of "Hamburger party".  Reviwed on 2020-04-16 11:49:48.867429Great food');

-- --------------------------------------------------------

--
-- Table structure for table `conlontj_customers`
--

CREATE TABLE IF NOT EXISTS `conlontj_customers` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `subscribed` varchar(5) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `conlontj_customers`
--

INSERT INTO `conlontj_customers` (`id`, `fname`, `lname`, `email`, `password`, `subscribed`) VALUES
(1, 'Testguy', 'Test', 'abcde@a.com', '', 'True'),
(2, 'Testguy', 'newname', 'a@a.com', '', 'True'),
(3, 'Tom', 'Test', 'b@a.com', '123', 'True'),
(4, 'Testguy', 'Test', 'a@a.com', '12345', 'True'),
(6, 'Tyler', 'Conlon', 'admin@tyconpowered.com', '123', 'True');

-- --------------------------------------------------------

--
-- Table structure for table `conlontj_events`
--

CREATE TABLE IF NOT EXISTS `conlontj_events` (
  `eid` int(5) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `start` datetime NOT NULL,
  `end` datetime NOT NULL,
  PRIMARY KEY (`eid`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `conlontj_events`
--

INSERT INTO `conlontj_events` (`eid`, `name`, `start`, `end`) VALUES
(1, 'End of social distancing party', '2020-05-05 18:00:00', '2020-05-06 18:15:00'),
(2, 'Hamburger party', '2020-04-16 12:00:00', '2020-04-16 14:00:00');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
