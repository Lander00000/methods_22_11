-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 27, 2022 at 10:17 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `methods`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE IF NOT EXISTS `book` (
  `bookid` int(11) NOT NULL,
  `isbn` varchar(20) NOT NULL,
  `title` varchar(50) NOT NULL,
  `author` varchar(50) NOT NULL,
  `published` varchar(30) NOT NULL,
  `stock` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `genre` varchar(255) NOT NULL,
  PRIMARY KEY(`bookid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS`user` (
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `name` varchar(50) NOT NULL,
  `shippinginfo` varchar(50) NOT NULL,
  `paymentinfo` varchar(50) NOT NULL,
  PRIMARY KEY(`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE IF NOT EXISTS `cart` (
  `username` varchar(30) NOT NULL,
  `b1` INT NOT NULL DEFAULT 0,
  `b2` INT NOT NULL DEFAULT 0,
  `b3` INT NOT NULL DEFAULT 0,
  `b4` INT NOT NULL DEFAULT 0,
  `b5` INT NOT NULL DEFAULT 0,
  `b6` INT NOT NULL DEFAULT 0,
  `b7` INT NOT NULL DEFAULT 0,
  `b8` INT NOT NULL DEFAULT 0,
  `b9` INT NOT NULL DEFAULT 0,
  `b10` INT NOT NULL DEFAULT 0,
  PRIMARY KEY(`username`),
  CONSTRAINT `cartowner`
    FOREIGN KEY (`username`)
    REFERENCES `user` (`username`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
    ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

CREATE TABLE IF NOT EXISTS `transaction` (
  `transactionid` int(11) NOT NULL,
  `username` varchar(30) NOT NULL,
  `purchaseList` varchar(300) NOT NULL,
  `cost` int(11) NOT NULL,
  `date` varchar(30) NOT NULL,
  PRIMARY KEY(`transactionid`),
  CONSTRAINT `transacter`
    FOREIGN KEY (`username`)
    REFERENCES `user` (`username`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


--
-- Indexes for dumped tables
--

--
-- Indexes for table `book`
--
--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `book`
--
ALTER TABLE `book`
  MODIFY `bookid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transaction`
--
ALTER TABLE `transaction`
  MODIFY `transactionid` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;



INSERT INTO user VALUES
("jack101","doghater","Jack","333 State St., Washington DC 30942", "71580898843392039 9/23 331"),
("these222", "nt5gtm3", "Robert", "101 Ground Blvd., Denver CO 53192", "4929553223512453 1/24 515"),
("barryobama","m1ch3ll3","Barack","89 Portside Cir., St. Louis MI 10221", "2931738930448451 3/26 843"),
("will3312","p455w0rd","Will","102 Grove St., Los Angeles CA, 90009", "4355203324685542 6/28 750"),
("leomessireal","g00000000l","Messi","202 Futbol St., Seattle WA 20135", "8592749254719577 3/25 832");

INSERT INTO book VALUES
("1", "9388369696", "The Art of War", "Sun Tzu", "475BC", 20, 16, "history"),
("2", "0679734503", "Crime and Punishment", "Fyodor Dostoyevsky", "1867", 10, 28, "literary fiction"),
("3", "0593158571", "Minecraft Redstone Handbook", "Mojang", "2022", 1, 10, "tutorial"),
("4", "1472288157", "FORTNITE Official - The Essential Guide", "Epic Games", "2022", 10, 20, "tutorial"),
("5", "8411981650", "The Communist Manifesto", "Karl Marx", "1848", 10, 3, "political theory"),
("6", "1338741160", "Five Nights at Freddy's: The Fourth Closet", "Scott Cawthon", "2021", 13, 20, "fiction"),
("7", "1613835051", "Jurassic Park", "Michael Crichton", "1990", 10, 10, "science fiction"),
("8", "0692528318", "The Federalist Papers", "Alexander Hamilton", "1788", 10, 20, "political theory"),
("9", "0399501487", "Lord of the Flies", "William Golding", "1954", 10, 13, "political theory"),
("10", "1580898843", "Baby Loves Coding!", "Ruth Spiro", "2018", 10, 12, "tutorial");

INSERT INTO cart VALUES
("jack101", 0,0,0,0,0,0,0,0,0,0),
("these222", 0,0,0,0,0,0,0,0,0,0),
("barryobama", 0,0,0,0,0,0,0,0,0,0),
("will3312", 0,0,0,0,0,0,0,0,0,0),
("leomessireal", 0,0,0,0,0,0,0,0,0,0);
