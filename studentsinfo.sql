-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 15, 2021 at 11:46 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crud_student`
--

-- --------------------------------------------------------

--
-- Table structure for table `studentsinfo`
--

CREATE TABLE `studentsinfo` (
  `stdid` int(10) NOT NULL,
  `firstname` varchar(45) NOT NULL,
  `lastname` varchar(45) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `address` varchar(45) NOT NULL,
  `mobile` bigint(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `studentsinfo`
--

INSERT INTO `studentsinfo` (`stdid`, `firstname`, `lastname`, `gender`, `address`, `mobile`) VALUES
(20124001, 'Naman', 'Shah', 'Male', 'Akota road, Sundarvan society', 8695412873),
(20124003, 'Bijal ', 'pandaya', 'Female', 'None', 9852165482),
(20124004, 'Dhruv', 'Patel', 'Male', 'None', 6755812926),
(20124007, 'Bhagirath', 'Rathod', 'Male', 'None', 8745812926),
(20124012, 'Chirag', 'Patel', 'Male', 'None', 9852165480),
(20124013, 'Sanhita', 'Patel', 'Female', 'None', 8745812979),
(20124023, 'Sowmya', 'Patel', 'Female', 'None', 8745812945),
(20124041, 'Krish', 'Savani', 'Male', 'None', 9852165487),
(20124045, 'Jashit', 'Khandari', 'Male', 'None', 9852165489),
(20124046, 'Rahulraj', 'Yadav', 'Male', '62/E Railway colony Pratapnagar, Vadodara', 7486980112),
(20124048, 'Vikas', 'Kumar', 'Male', 'None', 6549871263),
(20124072, 'Jugal', 'Gajjar', 'Male', 'None', 8745812935),
(20124081, 'Devesh', 'Patel', 'Male', 'None', 9874581297);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `studentsinfo`
--
ALTER TABLE `studentsinfo`
  ADD PRIMARY KEY (`stdid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
