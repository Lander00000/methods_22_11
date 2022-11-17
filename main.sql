CREATE TABLE IF NOT EXISTS `User` (
  `username` VARCHAR(30) NOT NULL,
  `password` VARCHAR(30) NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `shippinginfo` VARCHAR(50) NOT NULL,
  `paymentinfo` VARCHAR(50) NOT NULL,
  PRIMARY KEY(username))

CREATE TABLE IF NOT EXISTS `Cart` (
  `username` VARCHAR(30) NOT NULL,
  `b1` INT NOT NULL,
  `b2` INT NOT NULL,
  `b3` INT NOT NULL,
  `b4` INT NOT NULL,
  `b5` INT NOT NULL,
  `b6` INT NOT NULL,
  `b7` INT NOT NULL,
  `b8` INT NOT NULL,
  `b9` INT NOT NULL,
  `b10` INT NOT NULL,
  PRIMARY KEY(username))

CREATE TABLE IF NOT EXISTS `Book` (
  `bookid` VARCHAR(5) NOT NULL,
  `isbn` VARCHAR(20) NOT NULL,
  `title` VARCHAR(50) NOT NULL,
  `author` VARCHAR(50) NOT NULL,
  `published` VARCHAR(30) NOT NULL,
  `stock` INT NOT NULL,
  `price` INT NOT NULL,
  PRIMARY KEY(bookid))

CREATE TABLE IF NOT EXISTS `Transaction` (
  `transactionid` INT NOT NULL,
  `username` VARCHAR(30) NOT NULL,
  `purchaseList` VARCHAR(300) NOT NULL,
  `cost` INT NOT NULL,
  `date` VARCHAR(30) NOT NULL,
)
