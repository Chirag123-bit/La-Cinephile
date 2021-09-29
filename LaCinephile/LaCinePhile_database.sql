-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 29, 2021 at 06:33 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `la cinephile`
--
CREATE DATABASE IF NOT EXISTS `la cinephile` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `la cinephile`;

-- --------------------------------------------------------

--
-- Table structure for table `accounts_profile`
--

CREATE TABLE IF NOT EXISTS `accounts_profile` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `profile_pic` varchar(100) NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `city` varchar(30) NOT NULL,
  `district` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts_profile`
--

INSERT INTO `accounts_profile` (`id`, `firstname`, `lastname`, `email`, `phone`, `profile_pic`, `created_date`, `user_id`, `city`, `district`) VALUES
(2, 'Chirag', 'Simkhada', 'chiragsimkhada@gmail.com', '9868823820', 'static/profiles/onepiece.jpg', '2021-09-07 03:08:40.853887', 2, 'Sundarijal', 'Kathmandu'),
(8, 'Chirag', 'Simkhada', 'chiragsimkhada@gmail.com', '9868823820', 'sample_user.jpg', '2021-09-10 08:04:39.768174', 17, 'Sundarijal', 'Kathmandu'),
(9, 'Chirag', 'Simkhada', 'chiragsimkhada@gmail.com', '9868823820', 'sample_user.jpg', '2021-09-10 12:18:18.667787', 18, 'Sundarijal', 'Kathmandu'),
(10, 'Backup', 'Admin', 'backupadmin@gmail.com', '9868823820', 'sample_user.jpg', '2021-09-10 12:36:00.811661', 19, 'Sundarijal', 'Kathmandu'),
(16, 'Barbara', 'Sanford', 'BarbaraLSanford@armyspy.com', '9868823820', 'profiles/sample_user_MtXDN1I.jpg', '2021-09-28 03:35:26.015074', 28, 'Sundarijal', 'Kathmandu'),
(19, 'Test', 'User', 'ciwin65857@btkylj.com', '9868823820', 'sample_user.jpg', '2021-09-29 13:14:51.970554', 31, 'Sundarijal', 'Kathmandu');

-- --------------------------------------------------------

--
-- Table structure for table `accounts_user`
--

CREATE TABLE IF NOT EXISTS `accounts_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `f_name` varchar(20) NOT NULL,
  `l_name` varchar(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add movies', 7, 'add_movies'),
(26, 'Can change movies', 7, 'change_movies'),
(27, 'Can delete movies', 7, 'delete_movies'),
(28, 'Can view movies', 7, 'view_movies'),
(29, 'Can add movie', 8, 'add_movie'),
(30, 'Can change movie', 8, 'change_movie'),
(31, 'Can delete movie', 8, 'delete_movie'),
(32, 'Can view movie', 8, 'view_movie'),
(33, 'Can add up_ comming', 9, 'add_up_comming'),
(34, 'Can change up_ comming', 9, 'change_up_comming'),
(35, 'Can delete up_ comming', 9, 'delete_up_comming'),
(36, 'Can view up_ comming', 9, 'view_up_comming'),
(37, 'Can add now_ showing', 8, 'add_now_showing'),
(38, 'Can change now_ showing', 8, 'change_now_showing'),
(39, 'Can delete now_ showing', 8, 'delete_now_showing'),
(40, 'Can view now_ showing', 8, 'view_now_showing'),
(41, 'Can add user', 10, 'add_user'),
(42, 'Can change user', 10, 'change_user'),
(43, 'Can delete user', 10, 'delete_user'),
(44, 'Can view user', 10, 'view_user'),
(45, 'Can add category', 11, 'add_category'),
(46, 'Can change category', 11, 'change_category'),
(47, 'Can delete category', 11, 'delete_category'),
(48, 'Can view category', 11, 'view_category'),
(49, 'Can add hall', 12, 'add_hall'),
(50, 'Can change hall', 12, 'change_hall'),
(51, 'Can delete hall', 12, 'delete_hall'),
(52, 'Can view hall', 12, 'view_hall'),
(53, 'Can add categories', 13, 'add_categories'),
(54, 'Can change categories', 13, 'change_categories'),
(55, 'Can delete categories', 13, 'delete_categories'),
(56, 'Can view categories', 13, 'view_categories'),
(57, 'Can add profile', 14, 'add_profile'),
(58, 'Can change profile', 14, 'change_profile'),
(59, 'Can delete profile', 14, 'delete_profile'),
(60, 'Can view profile', 14, 'view_profile'),
(61, 'Can add hall_ timing', 15, 'add_hall_timing'),
(62, 'Can change hall_ timing', 15, 'change_hall_timing'),
(63, 'Can delete hall_ timing', 15, 'delete_hall_timing'),
(64, 'Can view hall_ timing', 15, 'view_hall_timing'),
(65, 'Can add movie_ timing', 16, 'add_movie_timing'),
(66, 'Can change movie_ timing', 16, 'change_movie_timing'),
(67, 'Can delete movie_ timing', 16, 'delete_movie_timing'),
(68, 'Can view movie_ timing', 16, 'view_movie_timing'),
(69, 'Can add movie_ hall', 16, 'add_movie_hall'),
(70, 'Can change movie_ hall', 16, 'change_movie_hall'),
(71, 'Can delete movie_ hall', 16, 'delete_movie_hall'),
(72, 'Can view movie_ hall', 16, 'view_movie_hall'),
(73, 'Can add ticket', 17, 'add_ticket'),
(74, 'Can change ticket', 17, 'change_ticket'),
(75, 'Can delete ticket', 17, 'delete_ticket'),
(76, 'Can view ticket', 17, 'view_ticket'),
(77, 'Can add booked', 18, 'add_booked'),
(78, 'Can change booked', 18, 'change_booked'),
(79, 'Can delete booked', 18, 'delete_booked'),
(80, 'Can view booked', 18, 'view_booked'),
(81, 'Can add ticket', 19, 'add_ticket'),
(82, 'Can change ticket', 19, 'change_ticket'),
(83, 'Can delete ticket', 19, 'delete_ticket'),
(84, 'Can view ticket', 19, 'view_ticket'),
(85, 'Can add purchase', 20, 'add_purchase'),
(86, 'Can change purchase', 20, 'change_purchase'),
(87, 'Can delete purchase', 20, 'delete_purchase'),
(88, 'Can view purchase', 20, 'view_purchase');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(2, 'pbkdf2_sha256$260000$FXEzVKU8ocahtIGAwPmwBZ$2DAUhP46BpklG4Vd5rGKr2E2X/9WxzvtFu1c4jZ2Uuk=', '2021-09-28 05:37:40.203704', 0, 'Chirag1', 'Chirag', 'Simkhada', 'chiragsimkhada@gmail.com', 0, 1, '2021-08-30 12:18:10.189678'),
(17, 'pbkdf2_sha256$260000$wpSGiKGDN5ZsH5pSDzSs32$KSyK41PLG8pT/alXUe2ezmSE/wfBrejKhTftKPqTzfU=', NULL, 0, 'ChiragS2', 'Chirag', 'Simkhada', 'chiragsimkhada@gmail.com', 0, 1, '2021-09-10 08:04:39.589992'),
(18, 'pbkdf2_sha256$260000$ZtOdahYDBE7PJWJdB1lJFe$dQtYI9ZLZ8YhsivaAEUaxYz2G8FA7bw9wMVcgyRhxMY=', '2021-09-29 14:33:16.014304', 1, 'HallAdmin', 'Chirag', 'Simkhada', 'chiragsimkhada@gmail.com', 1, 1, '2021-09-10 12:18:18.502878'),
(19, 'pbkdf2_sha256$260000$A90ArMFNSJI8vONR0R37uv$HOONCwro0qwV0vtrW5dwt+KUZiy+8wzFzaZ14khS6Iw=', '2021-09-29 14:12:14.604171', 1, 'BackupAdmin', 'Backup', 'Admin', 'backupadmin@gmail.com', 1, 1, '2021-09-10 12:36:00.642983'),
(28, 'pbkdf2_sha256$260000$UXkpRbcQx6jiYGEa2pX6Fa$tR3NqWXuhMb1T++O2w+5+Z8/wE5svW/+3oHkIMbdks8=', '2021-09-29 14:31:59.221106', 0, 'Barbara', 'Barbara', 'Sanford', 'BarbaraLSanford@armyspy.com', 0, 1, '2021-09-28 03:35:25.506988'),
(31, 'pbkdf2_sha256$260000$95UcdGWipP1379THSCxuFc$1IAn0P6V1B5j/g/XHtxSwUYN99GCMsSahBAIHUurtIY=', '2021-09-29 14:11:47.028293', 0, 'TestUser', 'Test', 'User', 'ciwin65857@btkylj.com', 0, 1, '2021-09-29 13:14:51.750144');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=302 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(226, '2021-09-28 07:28:16.604372', '154', 'The Grey', 3, '', 19, 19),
(227, '2021-09-28 07:28:16.607476', '153', 'The Grey', 3, '', 19, 19),
(228, '2021-09-28 07:28:16.611472', '152', 'The Grey', 3, '', 19, 19),
(229, '2021-09-28 07:28:16.616461', '151', 'The Grey', 3, '', 19, 19),
(230, '2021-09-28 07:28:16.618485', '150', 'The Grey', 3, '', 19, 19),
(231, '2021-09-28 07:28:16.621445', '149', 'The Grey', 3, '', 19, 19),
(232, '2021-09-28 07:28:16.623439', '148', 'The Grey', 3, '', 19, 19),
(233, '2021-09-28 07:28:16.625434', '147', 'The Grey', 3, '', 19, 19),
(234, '2021-09-28 07:28:16.627429', '146', 'The Grey', 3, '', 19, 19),
(235, '2021-09-28 07:28:16.630458', '145', 'The Grey', 3, '', 19, 19),
(236, '2021-09-28 07:28:16.632300', '144', 'The Grey', 3, '', 19, 19),
(237, '2021-09-28 07:28:16.633303', '143', 'The Grey', 3, '', 19, 19),
(238, '2021-09-28 07:28:16.635300', '142', 'The Grey', 3, '', 19, 19),
(239, '2021-09-28 07:28:16.637395', '141', 'The Grey', 3, '', 19, 19),
(240, '2021-09-28 07:28:16.638914', '140', 'The Grey', 3, '', 19, 19),
(241, '2021-09-28 07:28:16.641140', '139', 'The Grey', 3, '', 19, 19),
(242, '2021-09-28 07:28:16.645160', '138', 'The Grey', 3, '', 19, 19),
(243, '2021-09-28 07:28:16.648369', '137', 'The Grey', 3, '', 19, 19),
(244, '2021-09-28 07:28:16.651359', '136', 'The Grey', 3, '', 19, 19),
(245, '2021-09-28 07:28:16.654106', '135', 'The Grey', 3, '', 19, 19),
(246, '2021-09-28 07:28:16.656637', '134', 'The Grey', 3, '', 19, 19),
(247, '2021-09-28 07:28:16.658422', '133', 'The Grey', 3, '', 19, 19),
(248, '2021-09-28 07:28:16.660687', '132', 'The Grey', 3, '', 19, 19),
(249, '2021-09-28 07:28:16.662692', '131', 'The Grey', 3, '', 19, 19),
(250, '2021-09-28 07:28:16.664759', '130', 'The Grey', 3, '', 19, 19),
(251, '2021-09-28 07:28:16.667441', '129', 'The Grey', 3, '', 19, 19),
(252, '2021-09-28 07:28:16.669456', '128', 'The Grey', 3, '', 19, 19),
(253, '2021-09-28 07:28:16.671460', '127', 'The Grey', 3, '', 19, 19),
(254, '2021-09-28 07:28:16.675575', '126', 'The Grey', 3, '', 19, 19),
(255, '2021-09-28 07:28:16.678278', '125', 'The Grey', 3, '', 19, 19),
(256, '2021-09-28 07:28:16.681189', '124', 'The Grey', 3, '', 19, 19),
(257, '2021-09-28 07:28:16.684204', '123', 'The Grey', 3, '', 19, 19),
(258, '2021-09-28 07:28:16.686278', '122', 'The Grey', 3, '', 19, 19),
(259, '2021-09-28 07:28:16.688916', '121', 'The Grey', 3, '', 19, 19),
(260, '2021-09-28 07:28:16.691209', '120', 'The Grey', 3, '', 19, 19),
(261, '2021-09-28 07:28:16.694749', '119', 'The Grey', 3, '', 19, 19),
(262, '2021-09-28 07:28:16.696714', '118', 'The Grey', 3, '', 19, 19),
(263, '2021-09-28 07:28:16.699069', '117', 'The Grey', 3, '', 19, 19),
(264, '2021-09-28 07:28:16.701150', '116', 'The Grey', 3, '', 19, 19),
(265, '2021-09-28 07:28:16.703059', '115', 'The Grey', 3, '', 19, 19),
(266, '2021-09-28 07:28:16.705135', '114', 'The Grey', 3, '', 19, 19),
(267, '2021-09-28 07:28:16.708046', '113', 'The Grey', 3, '', 19, 19),
(268, '2021-09-28 07:28:16.709746', '112', 'The Grey', 3, '', 19, 19),
(269, '2021-09-28 07:28:16.711829', '111', 'The Grey', 3, '', 19, 19),
(270, '2021-09-28 07:28:16.715732', '110', 'The Grey', 3, '', 19, 19),
(271, '2021-09-28 07:28:16.717854', '109', 'The Grey', 3, '', 19, 19),
(272, '2021-09-28 07:28:16.720243', '108', 'The Grey', 3, '', 19, 19),
(273, '2021-09-28 07:28:16.722266', '107', 'The Grey', 3, '', 19, 19),
(274, '2021-09-28 07:28:16.724295', '106', 'The Grey', 3, '', 19, 19),
(275, '2021-09-28 07:28:16.727256', '105', 'The Grey', 3, '', 19, 19),
(276, '2021-09-28 07:28:16.729253', '104', 'The Grey', 3, '', 19, 19),
(277, '2021-09-28 07:28:16.732274', '103', 'The Grey', 3, '', 19, 19),
(278, '2021-09-28 07:28:16.734237', '102', 'The Grey', 3, '', 19, 19),
(279, '2021-09-28 07:28:16.735265', '101', 'The Grey', 3, '', 19, 19),
(280, '2021-09-28 07:28:16.737230', '100', 'The Grey', 3, '', 19, 19),
(281, '2021-09-28 07:28:16.739233', '99', 'The Grey', 3, '', 19, 19),
(282, '2021-09-28 07:28:16.741218', '98', 'The Grey', 3, '', 19, 19),
(283, '2021-09-28 07:28:16.743245', '97', 'The Grey', 3, '', 19, 19),
(284, '2021-09-28 07:28:16.745243', '96', 'The Grey', 3, '', 19, 19),
(285, '2021-09-28 07:28:16.748204', '95', 'The Grey', 3, '', 19, 19),
(286, '2021-09-28 07:28:16.751225', '94', 'The Grey', 3, '', 19, 19),
(287, '2021-09-28 07:28:16.753187', '93', 'The Grey', 3, '', 19, 19),
(288, '2021-09-28 07:28:16.755183', '92', 'The Grey', 3, '', 19, 19),
(289, '2021-09-28 07:28:16.757177', '91', 'The Grey', 3, '', 19, 19),
(290, '2021-09-28 07:28:16.760174', '90', 'The Grey', 3, '', 19, 19),
(291, '2021-09-28 07:28:16.763162', '89', 'The Grey', 3, '', 19, 19),
(292, '2021-09-28 07:28:16.765174', '88', 'The Grey', 3, '', 19, 19),
(293, '2021-09-28 07:28:16.767440', '87', 'The Grey', 3, '', 19, 19),
(294, '2021-09-28 07:28:16.769435', '86', 'The Grey', 3, '', 19, 19),
(295, '2021-09-28 07:28:16.770432', '85', 'The Grey', 3, '', 19, 19),
(296, '2021-09-28 07:28:16.772614', '84', 'The Grey', 3, '', 19, 19),
(297, '2021-09-28 07:28:16.774611', '83', 'The Grey', 3, '', 19, 19),
(298, '2021-09-28 07:28:16.777603', '82', 'The Grey', 3, '', 19, 19),
(299, '2021-09-28 07:28:16.780596', '81', 'The Grey', 3, '', 19, 19),
(300, '2021-09-28 07:28:16.782591', '80', 'The Grey', 3, '', 19, 19),
(301, '2021-09-28 07:28:16.783832', '79', 'The Grey', 3, '', 19, 19);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(14, 'accounts', 'profile'),
(10, 'accounts', 'user'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(18, 'halls', 'booked'),
(11, 'halls', 'category'),
(12, 'halls', 'hall'),
(15, 'halls', 'hall_timing'),
(16, 'halls', 'movie_hall'),
(20, 'halls', 'purchase'),
(19, 'halls', 'ticket'),
(7, 'movies', 'movies'),
(8, 'movies', 'now_showing'),
(9, 'movies', 'up_comming'),
(6, 'sessions', 'session'),
(13, 'tickets', 'categories'),
(17, 'tickets', 'ticket');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-08-23 15:40:22.903753'),
(2, 'auth', '0001_initial', '2021-08-23 15:40:23.432078'),
(3, 'admin', '0001_initial', '2021-08-23 15:40:23.551144'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-08-23 15:40:23.561228'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-08-23 15:40:23.569516'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-08-23 15:40:23.636982'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-08-23 15:40:23.687582'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-08-23 15:40:23.715509'),
(9, 'auth', '0004_alter_user_username_opts', '2021-08-23 15:40:23.728476'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-08-23 15:40:23.808737'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-08-23 15:40:23.813715'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-08-23 15:40:23.828678'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-08-23 15:40:23.851613'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-08-23 15:40:23.880535'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-08-23 15:40:23.903496'),
(16, 'auth', '0011_update_proxy_permissions', '2021-08-23 15:40:23.917458'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-08-23 15:40:23.936218'),
(18, 'movies', '0001_initial', '2021-08-23 15:40:23.970475'),
(19, 'movies', '0002_rename_movies_movie', '2021-08-23 15:40:23.996167'),
(20, 'movies', '0003_movie_summary', '2021-08-23 15:40:24.019918'),
(21, 'movies', '0004_auto_20210820_1124', '2021-08-23 15:40:24.027897'),
(22, 'movies', '0005_auto_20210821_1248', '2021-08-23 15:40:24.077568'),
(23, 'sessions', '0001_initial', '2021-08-23 15:40:24.115215'),
(24, 'movies', '0006_auto_20210824_1356', '2021-08-24 08:11:38.491770'),
(25, 'movies', '0007_up_comming_external_site', '2021-08-25 05:45:28.048365'),
(27, 'halls', '0001_initial', '2021-08-26 10:24:26.673536'),
(28, 'tickets', '0001_initial', '2021-08-26 10:40:26.023068'),
(29, 'halls', '0002_auto_20210901_1635', '2021-09-01 10:50:29.002222'),
(30, 'halls', '0002_auto_20210901_1640', '2021-09-01 10:55:34.453968'),
(31, 'halls', '0003_rename_movie_timing_movie_hall', '2021-09-01 10:56:56.277879'),
(32, 'halls', '0004_auto_20210902_1853', '2021-09-02 13:08:22.827679'),
(33, 'halls', '0005_auto_20210902_2256', '2021-09-02 17:11:11.279280'),
(34, 'halls', '0006_auto_20210902_2258', '2021-09-02 17:13:48.262117'),
(35, 'halls', '0007_auto_20210903_0737', '2021-09-03 01:55:33.137014'),
(36, 'halls', '0008_alter_movie_hall_date', '2021-09-03 01:55:33.144131'),
(37, 'halls', '0009_alter_movie_hall_date', '2021-09-03 01:58:53.313858'),
(38, 'tickets', '0002_categories_valid', '2021-09-03 09:24:42.516866'),
(39, 'tickets', '0003_remove_categories_valid', '2021-09-03 09:25:27.192963'),
(40, 'halls', '0010_movie_hall_discount', '2021-09-03 09:26:26.983697'),
(41, 'tickets', '0004_ticket', '2021-09-03 11:16:21.983612'),
(42, 'halls', '0011_movie_hall_booked', '2021-09-03 11:18:59.215611'),
(46, 'halls', '0012_auto_20210904_0814', '2021-09-07 02:27:11.843350'),
(47, 'halls', '0011_auto_20210907_0826', '2021-09-07 02:42:03.190808'),
(50, 'accounts', '0001_initial', '2021-09-07 02:54:03.603023'),
(51, 'accounts', '0002_profile_username', '2021-09-07 03:05:19.451646'),
(52, 'accounts', '0003_alter_profile_profile_pic', '2021-09-07 06:26:08.360235'),
(53, 'accounts', '0004_auto_20210907_1340', '2021-09-07 07:55:31.039176'),
(54, 'halls', '0012_auto_20210908_1353', '2021-09-08 08:08:52.134998'),
(55, 'halls', '0013_auto_20210909_0139', '2021-09-08 19:54:40.332499'),
(56, 'halls', '0014_alter_ticket_status', '2021-09-09 01:39:15.080216'),
(57, 'halls', '0015_auto_20210909_0840', '2021-09-09 02:55:17.924070'),
(58, 'halls', '0016_purchase_payment_completed', '2021-09-09 03:08:40.710539'),
(59, 'halls', '0017_alter_movie_hall_booked', '2021-09-09 08:48:52.343793'),
(60, 'accounts', '0005_alter_profile_profile_pic', '2021-09-10 07:47:07.237564'),
(61, 'accounts', '0006_alter_profile_profile_pic', '2021-09-10 07:53:07.416377'),
(62, 'accounts', '0007_alter_profile_profile_pic', '2021-09-10 07:55:11.780726'),
(63, 'movies', '0008_auto_20210910_1340', '2021-09-10 07:55:11.803696'),
(64, 'accounts', '0008_alter_profile_profile_pic', '2021-09-10 08:03:32.350702'),
(65, 'halls', '0018_alter_hall_category', '2021-09-10 10:16:42.571427'),
(66, 'halls', '0019_alter_hall_category', '2021-09-10 10:18:39.747989'),
(67, 'movies', '0009_auto_20210910_1737', '2021-09-10 11:53:14.926158'),
(68, 'movies', '0010_auto_20210910_1738', '2021-09-10 11:53:14.945109'),
(69, 'accounts', '0009_remove_profile_username', '2021-09-22 16:33:11.594312'),
(70, 'accounts', '0010_profile_username', '2021-09-22 16:35:25.041014'),
(71, 'accounts', '0011_remove_profile_username', '2021-09-22 16:38:00.246519');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('01g40ziprcdh7bwmskpd1662thm1blry', '.eJxVjDsOwjAQBe_iGlnx-htKes5grb1rHECOFCcV4u4QKQW0b2beS0Tc1hq3zkucSJwFiNPvljA_uO2A7thus8xzW5cpyV2RB-3yOhM_L4f7d1Cx12-d3TCQdwxckqKkcCxEmNiS0cYDaM6QymgUhVKg-ACkrNNGWwwWM4v3Bw4bOL0:1mMq9j:xnSqu75hN8_CdySCdoPmSDylCTfPNBveDq9K2BJC3MM', '2021-09-19 11:17:47.806674'),
('088d4qmqdh8ja42hdkdfa0cdf2k0e48v', '.eJxVjDsOwjAQBe_iGlnxJ46Xkp4zWBvvLg4gR4qTCnF3iJQC2jcz76USbmtJW-MlTaTOyqjT7zZifnDdAd2x3mad57ou06h3RR-06etM_Lwc7t9BwVa-dQTPyE6CRW8Fe7DEgD7nDlwQa8ABSLRCQy_IwXTRcPDk4uApuGDU-wPp6zeR:1mGEqe:5MOrjDtPbZe9b4RTpeovvEhwy5Q-GOhuCP2iIrVcm24', '2021-09-01 06:14:48.517000'),
('1y0iwtzhcnakia8yurrjoxw626lhm5t8', '.eJxVjEEOwiAQRe_C2pDpVKDj0r1nIFMYpGogKe3KeHfbpAvd_vfefyvP65L92mT2U1QXher0u40cnlJ2EB9c7lWHWpZ5GvWu6IM2fatRXtfD_TvI3PJWc8JoJQkRChl01Bsg5p4H6gJE4ETRIQ4OQ-hNBwjJba4FSWcHZNXnC-I4Nyc:1mNnxl:I3Dnjg_6BOpJ_QNrT5pducGYi61GxtSWPB2lSLcLCDM', '2021-09-22 03:09:25.064028'),
('27mpflem4l4p83d0pu8u71kwz9f3yku9', 'e30:1mNQAJ:zfQQoInewqsOF6i4MpzD2oloD4dZoVCeImGIl1JWvBs', '2021-09-21 01:44:47.272223'),
('4nbisxrfis7wkenwmeeb7fq38mtatwut', '.eJxVjDsOwjAQBe_iGlnx-htKes5grb1rHECOFCcV4u4QKQW0b2beS0Tc1hq3zkucSJwFiNPvljA_uO2A7thus8xzW5cpyV2RB-3yOhM_L4f7d1Cx12-d3TCQdwxckqKkcCxEmNiS0cYDaM6QymgUhVKg-ACkrNNGWwwWM4v3Bw4bOL0:1mMqBz:x4LZNwZCJLmHCWZ9gHusf4VncO56UpXqdU4B4ZRFsU0', '2021-09-19 11:20:07.166259'),
('8777hhfq8sl94wfals7u8q1hm8iunk2r', '.eJxVjDsOwjAQBe_iGlnxJ46Xkp4zWBvvLg4gR4qTCnF3iJQC2jcz76USbmtJW-MlTaTOyqjT7zZifnDdAd2x3mad57ou06h3RR-06etM_Lwc7t9BwVa-dQTPyE6CRW8Fe7DEgD7nDlwQa8ABSLRCQy_IwXTRcPDk4uApuGDU-wPp6zeR:1mKe8W:3H5Kfor-TUKuKS86Cb4rINNkspoqiJd-rPbQ4hOAiN0', '2021-09-13 10:03:28.485602'),
('cuoat8jqmgvnhfczwhufew0lzozyy3c3', '.eJxVjMsKwyAQAP_FcxFfi9pj7_0GWd1NTVsMxOQU-u9FyKG9zgxziIT7VtPeeU0ziasw4vLLMpYXtyHoie2xyLK0bZ2zHIk8bZf3hfh9O9u_QcVex7YgEWltoEzBYiS24IiDdcogBKuyCjnjVIBK0N6Qc9ZHnxVHYA8sPl_5kTgu:1mTg3V:yTtdPpIqr1_Ow5-XQLhHImA_F6-ptt6yeTYtqIOJXwE', '2021-10-08 07:55:37.325532'),
('fh6iqgioeg9u2zsxv6xstinl5zerxxf8', '.eJxVjMsKwyAQAP_FcxFfi9pj7_0GWd1NTVsMxOQU-u9FyKG9zgxziIT7VtPeeU0ziasw4vLLMpYXtyHoie2xyLK0bZ2zHIk8bZf3hfh9O9u_QcVex7YgEWltoEzBYiS24IiDdcogBKuyCjnjVIBK0N6Qc9ZHnxVHYA8sPl_5kTgu:1mUt8i:ZQTKPSroceqB9RfM9YbEC3ea7UXfenTGPbmoOO_bXO4', '2021-10-11 16:06:00.745785'),
('foylh4yoy57xasd236naf7y0r9fa5t68', '.eJxVjDsOwjAQBe_iGln-7MY2JT1nsNY_HEC2FCcV4u4QKQW0b2bei3na1uq3kRc_J3ZmyE6_W6D4yG0H6U7t1nnsbV3mwHeFH3Twa0_5eTncv4NKo35r4VIxAtBEY6yTSQVQNpMspEASYtY5WpW0BCwoXAANShU7SVccxEmz9wfKXDbx:1mN6tm:O0PESuDxTQokLQGlUuJ2dDuscxEONkufx_b7OqcCyP4', '2021-09-20 05:10:26.139865'),
('hurijjlvl5is4i8h3otl5oi3u85q951o', '.eJxVjEEOwiAQRe_C2pDpVKDj0r1nIFMYpGogKe3KeHfbpAvd_vfefyvP65L92mT2U1QXher0u40cnlJ2EB9c7lWHWpZ5GvWu6IM2fatRXtfD_TvI3PJWc8JoJQkRChl01Bsg5p4H6gJE4ETRIQ4OQ-hNBwjJba4FSWcHZNXnC-I4Nyc:1mObCL:kh9M3zqupzcHYkm9qVzLrW3WTSkDAo96WFtmXAmMJKE', '2021-09-24 07:43:45.447391'),
('hynx1qtzwwe1b0s6szy30ysqrljmccth', '.eJxVjDsOwjAQBe_iGlnxJ46Xkp4zWBvvLg4gR4qTCnF3iJQC2jcz76USbmtJW-MlTaTOyqjT7zZifnDdAd2x3mad57ou06h3RR-06etM_Lwc7t9BwVa-dQTPyE6CRW8Fe7DEgD7nDlwQa8ABSLRCQy_IwXTRcPDk4uApuGDU-wPp6zeR:1mI7e1:bD-OarnxP-G9ap0-qFbhaF52AZ2Tz0eD988W8JAi99k', '2021-09-06 10:57:33.635702'),
('jrt9ibzuse5dm19mfvdqoa43ys3z1i62', '.eJxVjDsOwjAQBe_iGlnxJ46Xkp4zWBvvLg4gR4qTCnF3iJQC2jcz76USbmtJW-MlTaTOyqjT7zZifnDdAd2x3mad57ou06h3RR-06etM_Lwc7t9BwVa-dQTPyE6CRW8Fe7DEgD7nDlwQa8ABSLRCQy_IwXTRcPDk4uApuGDU-wPp6zeR:1mJCaA:r-HCdQuNwLHQsXEeNkNIq27Y-Z54b6l2WKcV6rd38OE', '2021-09-09 10:26:02.904431'),
('jz97sn8ombi7ma4oh1oepj2f59cn75qq', '.eJxVjEEOwiAQRe_C2pABi4BL9z0DmYFBqgaS0q6Md7dNutDtf-_9twi4LiWsnecwJXEVyonT70gYn1x3kh5Y703GVpd5Irkr8qBdji3x63a4fwcFe9lqPQAQOusMqcs5Wh8tEBmmwWXrSCtUHDMZzEoxZ5_IGoCcwWswmyk-Xw2VOIQ:1mVae4:jjOvutAxHRejDdD-frz2AKUt7ptAzpZIR2bKf9orlLY', '2021-10-13 14:33:16.016348'),
('knjz8thenex1xkdrmlausjjn5yyskjp8', '.eJxVjDsOwjAQBe_iGlnx-htKes5grb1rHECOFCcV4u4QKQW0b2beS0Tc1hq3zkucSJwFiNPvljA_uO2A7thus8xzW5cpyV2RB-3yOhM_L4f7d1Cx12-d3TCQdwxckqKkcCxEmNiS0cYDaM6QymgUhVKg-ACkrNNGWwwWM4v3Bw4bOL0:1mNDt2:AR9InvJNbIuX-w28Ln2v60FtIaDKjCOLTNXBx4SjtqI', '2021-09-20 12:38:08.874976'),
('pl84wenfsxkuhgm3oaqee7dlxxnrfq9b', '.eJxVjEEOwiAQRe_C2pDpVKDj0r1nIFMYpGogKe3KeHfbpAvd_vfefyvP65L92mT2U1QXher0u40cnlJ2EB9c7lWHWpZ5GvWu6IM2fatRXtfD_TvI3PJWc8JoJQkRChl01Bsg5p4H6gJE4ETRIQ4OQ-hNBwjJba4FSWcHZNXnC-I4Nyc:1mNoIk:UHGLuYTKDZCB0on7H9FfciOfkmruLwPlhngdkFoxrBM', '2021-09-22 03:31:06.654692'),
('qs1pmc24tofw2yd1ccjrkefl3mvwtb2o', '.eJxVjEEOwiAQRe_C2pDpVKDj0r1nIFMYpGogKe3KeHfbpAvd_vfefyvP65L92mT2U1QXher0u40cnlJ2EB9c7lWHWpZ5GvWu6IM2fatRXtfD_TvI3PJWc8JoJQkRChl01Bsg5p4H6gJE4ETRIQ4OQ-hNBwjJba4FSWcHZNXnC-I4Nyc:1mNo2I:DMnQ7rFJOablDE_I3CdA5aeQFLKQwNCb-uPGtdVCnTs', '2021-09-22 03:14:06.932087'),
('qw1vd5mz79qv9ib7z2d9uip8oj4nlgm9', '.eJxVjDsOwjAQBe_iGlnxJ46Xkp4zWBvvLg4gR4qTCnF3iJQC2jcz76USbmtJW-MlTaTOyqjT7zZifnDdAd2x3mad57ou06h3RR-06etM_Lwc7t9BwVa-dQTPyE6CRW8Fe7DEgD7nDlwQa8ABSLRCQy_IwXTRcPDk4uApuGDU-wPp6zeR:1mIRXN:7ZhzBb1JQGe-SbwYpGINVxstQ4QbaHJYEq_1cblSSZc', '2021-09-07 08:12:01.023669'),
('t68ggf7heijnp67e7igfieuzntueq17a', '.eJxVjDsOwjAQBe_iGlnxJ46Xkp4zWBvvLg4gR4qTCnF3iJQC2jcz76USbmtJW-MlTaTOyqjT7zZifnDdAd2x3mad57ou06h3RR-06etM_Lwc7t9BwVa-dQTPyE6CRW8Fe7DEgD7nDlwQa8ABSLRCQy_IwXTRcPDk4uApuGDU-wPp6zeR:1mJWOM:QQqwzo4xMLq7YuEd3nF1Fqn3ZYIlPaIXDtxCL5GqLVo', '2021-09-10 07:35:10.369381'),
('tdgck1qcufby983nune8zmnirg53apew', '.eJxVjEEOwiAQRe_C2pDpVKDj0r1nIFMYpGogKe3KeHfbpAvd_vfefyvP65L92mT2U1QXher0u40cnlJ2EB9c7lWHWpZ5GvWu6IM2fatRXtfD_TvI3PJWc8JoJQkRChl01Bsg5p4H6gJE4ETRIQ4OQ-hNBwjJba4FSWcHZNXnC-I4Nyc:1mO0Yb:I7YineFg960JY5PiQzUS160KnwvUmWcQEEksb-tdIA0', '2021-09-22 16:36:17.118865'),
('v9t9nru8v884j28w15j96flzvd1h2aj9', '.eJxVjDsOwjAQBe_iGlnx-htKes5grb1rHECOFCcV4u4QKQW0b2beS0Tc1hq3zkucSJwFiNPvljA_uO2A7thus8xzW5cpyV2RB-3yOhM_L4f7d1Cx12-d3TCQdwxckqKkcCxEmNiS0cYDaM6QymgUhVKg-ACkrNNGWwwWM4v3Bw4bOL0:1mMq9H:Yc93n0ivUcpkhhv2YXEJLhy05jqf7NZHdnCGrlIe8X8', '2021-09-19 11:17:19.127628'),
('y69s3xsbj2xvlsa00ne959cga2i3ao82', '.eJxVjDsOwjAQBe_iGlnxJ46Xkp4zWBvvLg4gR4qTCnF3iJQC2jcz76USbmtJW-MlTaTOyqjT7zZifnDdAd2x3mad57ou06h3RR-06etM_Lwc7t9BwVa-dQTPyE6CRW8Fe7DEgD7nDlwQa8ABSLRCQy_IwXTRcPDk4uApuGDU-wPp6zeR:1mLf40:LKnuIvMwNVArsSLL3kENZgQGflP_1cCNKF4NaOONyqA', '2021-09-16 05:15:00.500879'),
('yslbsuu54svn6fwel6kanrt7oww4480t', '.eJxVjDsOwjAQBe_iGlnxJ46Xkp4zWBvvLg4gR4qTCnF3iJQC2jcz76USbmtJW-MlTaTOyqjT7zZifnDdAd2x3mad57ou06h3RR-06etM_Lwc7t9BwVa-dQTPyE6CRW8Fe7DEgD7nDlwQa8ABSLRCQy_IwXTRcPDk4uApuGDU-wPp6zeR:1mGxGT:Ix6JA1PLeRIbB7SDW-spONboeLV50DCb4vOgIbn6wf0', '2021-09-03 05:40:25.279000');

-- --------------------------------------------------------

--
-- Table structure for table `halls_category`
--

CREATE TABLE IF NOT EXISTS `halls_category` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `price` double NOT NULL,
  `color_code` varchar(7) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `halls_category`
--

INSERT INTO `halls_category` (`id`, `name`, `price`, `color_code`) VALUES
(1, 'GOLD', 300, '#D4AF37'),
(2, 'PLATINUM', 500, '#2ab0b1'),
(3, 'PREMIUM', 550, '#64bc46');

-- --------------------------------------------------------

--
-- Table structure for table `halls_hall`
--

CREATE TABLE IF NOT EXISTS `halls_hall` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `category_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `halls_hall_category_id_5b26df3e_fk_halls_category_id` (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `halls_hall`
--

INSERT INTO `halls_hall` (`id`, `name`, `category_id`) VALUES
(2, 'Cine A', 1),
(3, 'Cine B', 2),
(6, 'Cine E', 3),
(9, 'Cine C', 1),
(10, 'Cin H', 2),
(13, 'Test', 1);

-- --------------------------------------------------------

--
-- Table structure for table `halls_hall_timing`
--

CREATE TABLE IF NOT EXISTS `halls_hall_timing` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `time` varchar(100) NOT NULL,
  `day` varchar(100) NOT NULL,
  `hall_id` bigint(20) NOT NULL,
  `movie_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `halls_hall_timing_hall_id_b97c92c7_fk_halls_hall_id` (`hall_id`),
  KEY `halls_hall_timing_movie_id_1e44fd90_fk_movies_now_showing_id` (`movie_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `halls_hall_timing`
--

INSERT INTO `halls_hall_timing` (`id`, `time`, `day`, `hall_id`, `movie_id`) VALUES
(1, '1', '1', 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `halls_movie_hall`
--

CREATE TABLE IF NOT EXISTS `halls_movie_hall` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `time` varchar(100) NOT NULL,
  `hall_id` bigint(20) NOT NULL,
  `movie_id` bigint(20) NOT NULL,
  `date` date NOT NULL,
  `discount` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `halls_movie_timing_hall_id_6e830ec8_fk_halls_hall_id` (`hall_id`),
  KEY `halls_movie_timing_movie_id_f844d229_fk_movies_now_showing_id` (`movie_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `halls_movie_hall`
--

INSERT INTO `halls_movie_hall` (`id`, `time`, `hall_id`, `movie_id`, `date`, `discount`) VALUES
(1, '11AM - 2PM', 2, 1, '2021-10-27', 1),
(2, '7AM - 10AM', 3, 2, '2021-10-04', 1),
(8, '3PM - 6PM', 10, 3, '2021-10-24', 1),
(9, '3PM - 6PM', 6, 5, '2021-10-20', 1),
(10, '7PM - 10PM', 6, 9, '2021-10-27', 1),
(11, '7PM - 10PM', 3, 7, '2021-10-28', 1),
(15, '7PM - 10PM', 13, 17, '2021-10-29', 1);

-- --------------------------------------------------------

--
-- Table structure for table `halls_purchase`
--

CREATE TABLE IF NOT EXISTS `halls_purchase` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `status` varchar(100) NOT NULL,
  `seats` varchar(100) DEFAULT NULL,
  `price` int(11) NOT NULL,
  `discount_id` bigint(20) NOT NULL,
  `movie_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `payment_completed` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `halls_purchase_discount_id_592b5c63_fk_tickets_categories_id` (`discount_id`),
  KEY `halls_purchase_movie_id_0f6cefd8_fk_halls_movie_hall_id` (`movie_id`),
  KEY `halls_purchase_user_id_c98b1978_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `halls_purchase`
--

INSERT INTO `halls_purchase` (`id`, `status`, `seats`, `price`, `discount_id`, `movie_id`, `user_id`, `payment_completed`) VALUES
(1, 'Booked', 'a8', 50, 6, 1, 2, 0),
(2, 'Booked', 'a8', 50, 6, 1, 2, 0),
(3, 'Booked', 'd7', 50, 6, 1, 2, 0),
(4, 'Booked', 'e3', 50, 6, 1, 2, 0),
(5, 'Booked', 'e3', 50, 6, 1, 2, 0),
(6, 'Booked', 'a7', 50, 6, 1, 2, 0),
(7, 'Booked', 'b7', 50, 6, 1, 2, 0),
(8, 'Booked', 'f1', 50, 6, 1, 2, 0),
(9, 'Booked', 'f1', 50, 6, 1, 2, 0),
(10, 'Booked', 'a2', 50, 6, 1, 2, 0),
(11, 'Booked', 'a2', 50, 6, 1, 2, 0),
(12, 'Booked', 'b8', 50, 6, 1, 2, 0),
(13, 'Booked', 'b8', 50, 6, 1, 2, 0),
(14, 'Booked', 'a6', 50, 6, 1, 2, 0),
(15, 'Booked', 'a5', 50, 6, 1, 2, 0),
(16, 'Booked', 'd8', 50, 6, 1, 2, 0),
(17, 'Purchased', 'b6', 50, 6, 1, 2, 1),
(18, 'Purchased', 'b5', 50, 6, 1, 2, 1),
(19, 'Purchased', 'e8', 50, 6, 1, 2, 1),
(20, 'Purchased', 'e7', 50, 6, 1, 2, 1),
(21, 'Purchased', 'c7', 50, 6, 1, 2, 1),
(22, 'Purchased', 'b4', 50, 6, 1, 2, 1),
(23, 'Purchased', 'a3', 50, 6, 1, 2, 1),
(24, 'Purchased', 'a3', 300, 1, 2, 2, 1),
(25, 'Purchased', 'a6', 300, 1, 2, 2, 1),
(26, 'Purchased', 'c8', 50, 6, 1, 2, 1),
(27, 'Purchased', 'd3', 50, 6, 1, 2, 0),
(28, 'Purchased', 'b2', 50, 6, 1, 2, 0),
(29, 'Purchased', 'd7', 50, 6, 1, 2, 0),
(30, 'Purchased', 'f8', 50, 6, 1, 2, 0),
(31, 'Purchased', 'c5', 300, 6, 9, 2, 0),
(32, 'Purchased', 'f7', 400, 3, 8, 2, 0),
(33, 'Purchased', 'c7', 50, 6, 1, 2, 0),
(36, 'Purchased', 'a6', 200, 3, 15, 31, 1);

-- --------------------------------------------------------

--
-- Table structure for table `halls_ticket`
--

CREATE TABLE IF NOT EXISTS `halls_ticket` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `seats` varchar(2) DEFAULT NULL,
  `discount_id` bigint(20) NOT NULL,
  `movie_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `status` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `halls_ticket_discount_id_d8369aa1_fk_tickets_categories_id` (`discount_id`),
  KEY `halls_ticket_movie_id_bcb30ef4_fk_halls_movie_hall_id` (`movie_id`),
  KEY `halls_ticket_user_id_fdc40588_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=161 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `halls_ticket`
--

INSERT INTO `halls_ticket` (`id`, `seats`, `discount_id`, `movie_id`, `user_id`, `status`) VALUES
(57, 'a3', 6, 1, 2, 'Purchased'),
(58, 'c8', 1, 2, 2, 'Purchased'),
(59, 'b6', 6, 1, 2, 'Canceled'),
(60, 'a3', 1, 2, 2, 'Purchased'),
(61, 'f4', 1, 1, 2, 'Booked'),
(62, 'f6', 6, 1, 2, 'Booked'),
(63, 'a6', 1, 2, 2, 'Purchased'),
(64, 'c8', 6, 1, 2, 'Purchased'),
(65, 'd3', 6, 1, 2, 'Purchased'),
(66, 'b2', 6, 1, 2, 'Purchased'),
(67, 'd7', 6, 1, 2, 'Purchased'),
(68, 'a8', 6, 1, 2, 'Booked'),
(69, 'f8', 6, 1, 2, 'Purchased'),
(70, 'e8', 6, 1, 2, 'Booked'),
(71, 'f8', 3, 8, 2, 'Canceled'),
(72, 'c8', 6, 9, 2, 'Booked'),
(73, 'c7', 6, 9, 2, 'Purchased'),
(74, 'c5', 6, 9, 2, 'Purchased'),
(75, 'e8', 6, 9, 2, 'Purchased'),
(76, 'f7', 3, 8, 2, 'Purchased'),
(77, 'c7', 6, 1, 2, 'Purchased'),
(78, 'a8', 6, 10, 2, 'Canceled'),
(155, 'a7', 3, 11, 28, 'Canceled'),
(159, 'a6', 3, 15, 31, 'Purchased'),
(160, 'a6', 6, 1, 31, 'Canceled');

-- --------------------------------------------------------

--
-- Table structure for table `movies_now_showing`
--

CREATE TABLE IF NOT EXISTS `movies_now_showing` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `poster` varchar(100) NOT NULL,
  `trailer` varchar(200) NOT NULL,
  `imdb` double NOT NULL,
  `desc` longtext NOT NULL,
  `actors` varchar(300) NOT NULL,
  `director` varchar(100) NOT NULL,
  `summary` varchar(500) NOT NULL,
  `background` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `movies_now_showing`
--

INSERT INTO `movies_now_showing` (`id`, `name`, `poster`, `trailer`, `imdb`, `desc`, `actors`, `director`, `summary`, `background`) VALUES
(1, 'Aladdin', 'static/images/movies/pos-1.jpg', 'https://www.youtube.com/embed/foyufD52aog?autoplay=1&mute=1&enablejsapi=1&hd=1', 6.9, 'Aladdin is a lovable street urchin who meets Princess Jasmine, the beautiful daughter of the sultan of Agrabah. While visiting her exotic palace, Aladdin stumbles upon a magic oil lamp that unleashes a powerful, wisecracking, larger-than-life genie. As Aladdin and the genie start to become friends, they must soon embark on a dangerous mission to stop the evil sorcerer, Jafar, from overthrowing young Jasmine\'s kingdom.', 'Will Smith, Mena Massoud, Naomi Scott', 'Guy Ritchie', 'A kind-hearted street urchin and a power-hungry Grand Vizier vie for a magic lamp that has the power to make their deepest wishes come true. Lets watch the journey of Aladin.', 'Aladin.jpg'),
(2, 'Joker', 'static/images/movies/Joker-poster.jpg', 'https://www.youtube.com/embed/zAGVQLHvwOY?autoplay=1&hd=1&mute=1&enablejsapi=1', 8.9, 'Forever alone in a crowd, failed comedian Arthur Fleck seeks connection as he walks the streets of Gotham City. Arthur wears two masks -- the one he paints for his day job as a clown, and the guise he projects in a futile attempt to feel like he\'s part of the world around him. Isolated, bullied and disregarded by society, Fleck begins a slow descent into madness as he transforms into the criminal mastermind known as the Joker.', 'Joaquin Phoenix, Robert De Niro, Zazie Beetz', 'Todd Phillips', 'Party clown and aspiring stand-up comedian Arthur Fleck lives with his mother, Penny, in Gotham City, which is rife with crime and unemployment. This movie follow this journey of Arthur', 'joker.png'),
(3, 'Avengers: Endgame', 'static/images/movies/pos-3_Mrp4sZG.jpg', 'https://www.youtube.com/embed/TcMBFSGVi1c?autoplay=1&enablejsapi=1&hd=1&mute=1', 8.4, 'Adrift in space with no food or water, Tony Stark sends a message to Pepper Potts as his oxygen supply starts to dwindle. Meanwhile, the remaining Avengers -- Thor, Black Widow, Captain America and Bruce Banner -- must figure out a way to bring back their vanquished allies for an epic showdown with Thanos -- the evil demigod who decimated the planet and the universe.', 'Robert Downey Jr.,  Chris Evans, Mark Ruffalo,', 'Russo brothers', 'In 2018, twenty-three days after Thanos killed half of all life in the universe,[N 1] Carol Danvers rescues Tony Stark and Nebula from deep space and they reunite with Avengers', 'endgame.jpg'),
(4, 'Vampire Hunter', 'static/images/movies/pos-4.jpg', 'https://www.youtube.com/embed/wZp7eBStN1U?autoplay=1&mute=1&enablejsapi=1&hd=1', 5.9, 'At the age of 9, Abraham Lincoln witnesses his mother being killed by a vampire, Jack Barts. Some 10 years later, he unsuccessfully tries to eliminate Barts but in the process makes the acquaintance of Henry Sturgess who teaches him how to fight and what is required to kill a vampire. The quid pro quo is that Abe will kill only those vampires that Henry directs him to. Abe relocates to Springfield where he gets a job as a store clerk while he studies the law and kills vampires by night.', 'Benjamin Walker, Dominic Cooper, Anthony Mackie', 'Timur Bekmambetov', 'In 1818, Abraham Lincoln lives in Indiana with his parents, Nancy and Thomas, who works at a plantation owned by Jack Barts.', 'vampire.jpg'),
(5, 'Men In Black', 'static/images/movies/pos-5.jpg', 'https://www.youtube.com/embed/BV-WEb2oxLk?autoplay=1&mute=1&enablejsapi=1&hd=1', 5.6, 'The Men in Black have expanded to cover the globe but so have the villains of the universe. To keep everyone safe, decorated Agent H and determined rookie M join forces -- an unlikely pairing that just might work. When aliens that can take the form of any human arrive on Earth, H and M embark on a globe-trotting adventure to save the agency -- and ultimately the world -- from their mischievous plans.', 'Chris Hemsworth, Tessa Thompson, Rebecca Ferguson', 'F. Gary Gray', 'Agent M, a probationary member of the MIB, teams up with Agent H and uncovers a sinister plot that reveals a traitor in the organisation aiding an alien invasion.', 'mib.jpg'),
(6, 'The Dark Night Rises', 'static/images/movies/pos-6.jpg', 'https://www.youtube.com/embed/g8evyE9TuYk?autoplay=1&mute=1&enablejsapi=1&hd=1', 8.4, 'A gang of criminals rob a Gotham City mob bank; the Joker manipulates them into murdering each other for a higher share until only he remains, escaping with the money. Batman, District Attorney Harvey Dent and Lieutenant Jim Gordon form an alliance to rid Gotham of organized crime.', 'Christian Bale, Michael Caine, Gary Oldman', 'Christopher Nolan', 'Bane, a masked terrorist and former member of the League of Shadows, abducts nuclear physicist Dr. Leonid Pavel from a CIA aircraft over Uzbekistan before crashing the aircraft.', 'dark.jpg'),
(7, 'Dora and City of Gold', 'static/images/movies/pos-7_pcaRxwM.jpg', 'https://www.youtube.com/embed/gUTtJjV852c?autoplay=1&mute=1&enablejsapi=1&hd=1', 6.1, 'Having spent most of her life exploring the jungle, nothing could prepare Dora for her most dangerous adventure yet -- high school. Accompanied by a ragtag group of teens and Boots the monkey, Dora embarks on a quest to save her parents while trying to solve the seemingly impossible mystery behind a lost Incan civilization.', 'Isabela Moner, Eugenio Derbez, Michael Pe±a', 'James Bobin', 'Deep in the Peruvian jungle, 6-year-old Dora Mßrquez, daughter of jungle explorers Cole and Elena, spends her days on adventures', 'dora.jpg'),
(8, 'Black Widow', 'static/images/movies/pos-8.jpg', 'https://www.youtube.com/embed/ybji16u608U?autoplay=1&mute=1&enablejsapi=1&hd=1', 6.8, 'In 1995, super-soldier Alexei Shostakov and Black Widow Melina Vostokoff work as Russian undercover agents, posing as a family in Ohio with Natasha Romanoff and Yelena Belova as their daughters. They steal S.H.I.E.L.D. intel and escape to Cuba where their boss, General Dreykov, has Romanoff and Belova taken to the Red Room for training. Years pass, during which Shostakov is imprisoned in Russia while Romanoff defects to S.H.I.E.L.D. after bombing Dreykov\'s Budapest office and apparently killing him and his young daughter Antonia.', 'Scarlett Johansson, Florence Pugh, David Harbour', 'Cate Shortland', 'Natasha Romanoff, aka Black Widow, confronts the darker parts of her ledger when a dangerous conspiracy with ties to her past arises.', 'widow.jpg'),
(9, 'The Grey', 'static/images/movies/pos-9.jpg', 'https://www.youtube.com/embed/eUP5Vr0lBvY?autoplay=1&mute=1&enablejsapi=1&hd=1', 6.8, 'John Ottway is a marksman for an oil company in Alaska, killing grey wolves that threaten the drillers. On his last day on the job, he sees a wolf pursuing a driller and shoots it, listening to the wolf’s final breath. That evening, Ottway writes a letter \"without purpose\" to his wife, Ana, explaining his plans to complete suicide, but does not follow through.\r\n\r\nThe next day, Ottway survives a plane crash with fellow oil workers, watching helplessly as Lewenden dies of his injuries. Ottway takes charge of the survivors and is attacked by a wolf and rescued by the group; they realize they are in the wolves\' territory and take turns keeping watch.', 'Liam Neeson, Frank Grillo, Dermot Mulroney', 'Joe Carnahan', 'John, a wolf hunter, is one of the eight survivors of a plane crash. He must fight off a pack of hungry wolves, mortal injuries and the icy elements to get himself and the survivors back to safety.', 'grey.jpg'),
(10, 'The Hobbit', 'static/images/movies/pos-10.jpg', 'https://www.youtube.com/embed/G0k3kHtyoqc?autoplay=1&mute=1&enablejsapi=1&hd=1', 7.8, 'Approaching his 111th birthday, the Hobbit Bilbo Baggins begins writing down the full story of his adventure 60 years earlier for the benefit of his nephew, Frodo.\r\n\r\nLong before Bilbo\'s involvement, the Dwarf king Thrór brought an era of prosperity for his kin under the Lonely Mountain until the arrival of the dragon Smaug. Destroying the nearby town of Dale, Smaug drove the Dwarves out of their mountain and took their hoard of gold. Thrór\'s grandson, Thorin, sees King Thranduil and his Wood-elves on a nearby hillside, and is dismayed when they leave rather than aid his people, resulting in Thorin\'s everlasting hatred of Elves.', 'Ian McKellen, Martin Freeman, Richard Armitage', 'Peter Jackson', 'The Hobbit is set within Tolkien\'s fictional universe and follows the quest of home-loving Bilbo Baggins, the titular hobbit, to win a share of the treasure guarded by Smaug the dragon.', 'hobbit.jpg'),
(11, 'Interstellar', 'static/images/movies/pos-11.jpg', 'https://www.youtube.com/embed/zSWdZVtXT7E?autoplay=1&mute=1&enablejsapi=1&hd=1', 8.6, 'In 2067, crop blights and dust storms threaten humanity\'s survival. Cooper, a widowed engineer and former NASA pilot turned farmer, lives with his father-in-law, Donald, his 15-year-old son, Tom Cooper, and 10-year-old daughter, Murphy \"Murph\" Cooper. After a dust storm, strange dust patterns inexplicably appear in Murphy\'s bedroom; she attributes the anomaly to a ghost. Cooper eventually deduces the patterns were caused by gravity variations and they represent geographic coordinates in binary code. Cooper follows the coordinates to a secret NASA facility headed by Professor John Brand.', 'Matthew McConaughey, Anne Hathaway, Jessica Chastain', 'Christopher Nolan', 'When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans.', 'inter_AAWWK2x.jpg'),
(12, 'Space Jam', 'static/images/movies/pos-12.jpg', 'https://www.youtube.com/embed/RCsEKvz2mxs?autoplay=1&mute=1&enablejsapi=1&hd=1', 4.6, 'In 1973, a young Michael Jordan tells his father, James, about his dreams of playing in the NBA. Twenty years later (1993), following his father\'s death, Jordan announces his retirement from basketball and pursues a baseball career.\r\n\r\nMeanwhile, in outer space, the amusement park Moron Mountain is in decline. Mr. Swackhammer, the park\'s proprietor, learns of the Looney Tunes from his minions, the Nerdlucks, and tasks them with abducting them as attractions. Upon their arrival beneath Earth\'s surface, Bugs Bunny and the other Looney Tunes note the Nerdlucks\' small stature and challenge them to a basketball game despite their lack of experience. After learning more of basketball, the Nerdlucks infiltrate various games, usurping the talents of Charles Barkley, Shawn Bradley, Patrick Ewing, Larry Johnson, and Muggsy Bogues. The Nerdlucks use these talents to transform into large, muscular versions of themselves, whom Sylvester refers to as Monstars. The easily intimidated Looney Tunes realize their need for professional help.', 'Michael Jordan, Billy West, Wayne Knight', 'Joe Pytka', 'Superstar LeBron James and his young son, Dom, get trapped in digital space by a rogue AI. To get home safely, LeBron teams up with Bugs Bunny, Daffy Duck and the rest of the Looney Tunes gang', 'space.jpg'),
(17, 'Harry Potter And The Deathly Hallow', 'static/images/movies/poster_sa6KG4V.jpg', 'https://www.youtube.com/embed/MxqsmsA8y5k', 8.1, 'A clash between good and evil awaits as young Harry, Ron and Hermione prepare for a final battle against Lord Voldemort. Harry has grown into a steely lad on a mission to rid the world of evil. The friends must search for the Horcruxes that keep the dastardly wizard immortal. Harry and Voldemort meet at Hogwarts Castle for an epic showdown where the forces of darkness may finally meet their match.', 'Daniel Radcliffe, Rupert Grint, Emma Watson', 'David Yates', 'After murdering Harry\'s parents, James and Lily Potter, evil Lord Voldemort puts a killing curse on Harry, then just a baby.', 'static/images/movies/wallpaper_7asrpT9.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `movies_up_comming`
--

CREATE TABLE IF NOT EXISTS `movies_up_comming` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `poster` varchar(100) NOT NULL,
  `trailer` varchar(200) NOT NULL,
  `summary` varchar(500) NOT NULL,
  `desc` longtext NOT NULL,
  `actors` varchar(300) NOT NULL,
  `director` varchar(100) NOT NULL,
  `release_date` varchar(50) NOT NULL,
  `background` varchar(100) DEFAULT NULL,
  `external_site` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `movies_up_comming`
--

INSERT INTO `movies_up_comming` (`id`, `name`, `poster`, `trailer`, `summary`, `desc`, `actors`, `director`, `release_date`, `background`, `external_site`) VALUES
(1, 'The King\'s Man', 'static/images/movies/kings_man.jpg', 'https://www.youtube.com/embed/5zdBG-iGfes', 'One man must race against time to stop history\'s worst tyrants and criminal masterminds as they get together to plot a war that could wipe out millions of people and destroy humanity.', 'The King\'s Man is an upcoming period action spy film directed by Matthew Vaughn from a screenplay by Vaughn and Karl Gajdusek and a story by Vaughn. The third instalment in the Kingsman film series, which is based on the comic book The Secret Service by Mark Millar and Dave Gibbons, the film serves as a prequel to 2014\'s Kingsman: The Secret Service and 2017\'s Kingsman: The Golden Circle.\r\n\r\nThe film features an ensemble cast that includes Ralph Fiennes, Gemma Arterton, Rhys Ifans, Matthew Goode, Tom Hollander, Harris Dickinson, Daniel Brⁿhl, Djimon Hounsou, and Charles Dance.', 'Ralph Fiennes, Gemma Arterton, Rhys Ifans', 'Matthew Vaughn', 'December 22, 2021', 'kingsman.jpg', 'https://www.imdb.com/title/tt6856242/'),
(2, 'Venom 2', 'static/images/movies/venom.jpg', 'https://www.youtube.com/embed/ueXkLEpJBPU', 'Tom Hardy returns to the big screen as the lethal protector Venom, one of MARVEL\'s greatest and most complex characters.). The film is directed by Andy Serkis from a screenplay .', 'Venom: Let There Be Carnage is an upcoming American superhero film featuring the Marvel Comics character Venom, produced by Columbia Pictures in association with Marvel and Tencent Pictures. Distributed by Sony Pictures Releasing, it is intended to be the second film in the Sony Pictures Universe of Marvel Characters and the sequel to Venom (2018). The film is directed by Andy Serkis from a screenplay by Kelly Marcel, based on a story she wrote with Tom Hardy who stars as Eddie Brock / Venom alongside Michelle Williams, Naomie Harris, Reid Scott, Stephen Graham, and Woody Harrelson. In the film, Brock tries to reignite his career in journalism by interviewing serial killer Cletus Kasady (Harrelson), who becomes the host of an alien symbiote similar to Venom named Carnage.', 'Tom Hardy, Michelle Williams, Naomie Harris', 'Andy Serkis', 'October 15, 2021', 'venom.jpg', 'https://www.imdb.com/title/tt7097896/'),
(3, 'Shang-Chi', 'static/images/movies/sang_chi.jpg', 'https://www.youtube.com/embed/giWIr7U1deA', 'Martial-arts master Shang-Chi confronts the past he thought he left behind when he\'s drawn into the web of the mysterious Ten Rings organization. Shang-Chi is forced to confront his past after he is drawn into the Ten Rings.', 'Shang-Chi and the Legend of the Ten Rings is a 2021 American superhero film based on the Marvel Comics featuring the character Shang-Chi. Produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures, it is the 25th film in the Marvel Cinematic Universe (MCU). The film is directed by Destin Daniel Cretton from a screenplay he wrote with Dave Callaham and Andrew Lanham, from a story by Cretton and Callaham. It stars Simu Liu as Shang-Chi alongside Awkwafina, Meng\'er Zhang, Fala Chen, Florian Munteanu, Benedict Wong, Michelle Yeoh, and Tony Leung. In the film, Shang-Chi is forced to confront his past after he is drawn into the Ten Rings organization.', 'Simu Liu, Awkwafina, Meng\'er Zhang', 'Destin Daniel Cretton', 'August 16, 2021', 'Shang-chi.jpg', 'https://www.imdb.com/title/tt9376612/'),
(4, 'Eternals', 'static/images/movies/eternals.jpg', 'https://www.youtube.com/embed/x_me3xsvDgk', 'The Eternals, a race of immortal beings with superhuman powers who have secretly lived on Earth for thousands of years, reunite to battle the evil Deviants and protect Earth from their evil counterparts, the Deviants.', 'Eternals is an upcoming American superhero film based on the Marvel Comics race of the same name. Produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures, it is intended to be the 26th film in the Marvel Cinematic Universe (MCU). The film was directed by ChloΘ Zhao, who wrote the screenplay with Patrick Burleigh, Ryan Firpo, and Kaz Firpo. It stars an ensemble cast including Gemma Chan, Richard Madden, Kumail Nanjiani, Lia McHugh, Brian Tyree Henry, Lauren Ridloff, Barry Keoghan, Don Lee, Harish Patel, Kit Harington, Salma Hayek, and Angelina Jolie. In the film, the Eternals, an immortal alien race, emerge from hiding after thousands of years to protect Earth from their evil counterparts, the Deviants.', 'Gemma Chan, Richard Madden, Kumail Nanjiani', 'ChloΘ Zhao', 'November 5, 2021', 'eternals.png', 'https://www.imdb.com/title/tt9032400/'),
(5, 'No Way Home', 'static/images/movies/spidy.jpg', 'https://www.youtube.com/embed/b8gw1JEYE00', 'Spider-Man: No Way Home is an upcoming American superhero film based on the Marvel Comics character Spider-Man Spider-Man, alongside Zendaya, J. B. Smoove, Jacob Batalon, Marisa Tomei, Jamie Foxx', 'Spider-Man: No Way Home is an upcoming American superhero film based on the Marvel Comics character Spider-Man, co-produced by Columbia Pictures and Marvel Studios, and distributed by Sony Pictures Releasing. It is intended to be the sequel to Spider-Man: Homecoming (2017) and Spider-Man: Far From Home (2019), and the 27th film in the Marvel Cinematic Universe (MCU). The film was directed by Jon Watts, written by Chris McKenna and Erik Sommers, and stars Tom Holland as Peter Parker / Spider-Man, alongside Zendaya, J. B. Smoove, Jacob Batalon, Marisa Tomei, Jamie Foxx, Benedict Cumberbatch, and Alfred Molina.', 'Tom Holland, Zendaya, J. B. Smoove', 'ChloΘ Zhao', 'November 5, 2021', 'spiderman.jpg', 'https://www.imdb.com/title/tt10872600/');

-- --------------------------------------------------------

--
-- Table structure for table `tickets_categories`
--

CREATE TABLE IF NOT EXISTS `tickets_categories` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `discount` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tickets_categories`
--

INSERT INTO `tickets_categories` (`id`, `name`, `discount`) VALUES
(1, 'Morning Shows (Sunday To Saturday, 7 AM-10 AM)', 200),
(2, 'Weekday Shows (Monday & Thursday)', 100),
(3, 'Weekend Shows (Friday To Sunday)', 100),
(4, 'Public Holiday Shows', 0),
(5, 'New Movie Release Day (Monday To Thursday)', 0),
(6, 'Two Days Fun Days (Tuesday and Wednesday)', 250),
(7, 'No Discount', 0);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accounts_profile`
--
ALTER TABLE `accounts_profile`
  ADD CONSTRAINT `accounts_profile_user_id_49a85d32_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `halls_hall`
--
ALTER TABLE `halls_hall`
  ADD CONSTRAINT `halls_hall_category_id_5b26df3e_fk_halls_category_id` FOREIGN KEY (`category_id`) REFERENCES `halls_category` (`id`);

--
-- Constraints for table `halls_hall_timing`
--
ALTER TABLE `halls_hall_timing`
  ADD CONSTRAINT `halls_hall_timing_hall_id_b97c92c7_fk_halls_hall_id` FOREIGN KEY (`hall_id`) REFERENCES `halls_hall` (`id`),
  ADD CONSTRAINT `halls_hall_timing_movie_id_1e44fd90_fk_movies_now_showing_id` FOREIGN KEY (`movie_id`) REFERENCES `movies_now_showing` (`id`);

--
-- Constraints for table `halls_movie_hall`
--
ALTER TABLE `halls_movie_hall`
  ADD CONSTRAINT `halls_movie_timing_hall_id_6e830ec8_fk_halls_hall_id` FOREIGN KEY (`hall_id`) REFERENCES `halls_hall` (`id`),
  ADD CONSTRAINT `halls_movie_timing_movie_id_f844d229_fk_movies_now_showing_id` FOREIGN KEY (`movie_id`) REFERENCES `movies_now_showing` (`id`);

--
-- Constraints for table `halls_purchase`
--
ALTER TABLE `halls_purchase`
  ADD CONSTRAINT `halls_purchase_discount_id_592b5c63_fk_tickets_categories_id` FOREIGN KEY (`discount_id`) REFERENCES `tickets_categories` (`id`),
  ADD CONSTRAINT `halls_purchase_movie_id_0f6cefd8_fk_halls_movie_hall_id` FOREIGN KEY (`movie_id`) REFERENCES `halls_movie_hall` (`id`),
  ADD CONSTRAINT `halls_purchase_user_id_c98b1978_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `halls_ticket`
--
ALTER TABLE `halls_ticket`
  ADD CONSTRAINT `halls_ticket_discount_id_d8369aa1_fk_tickets_categories_id` FOREIGN KEY (`discount_id`) REFERENCES `tickets_categories` (`id`),
  ADD CONSTRAINT `halls_ticket_movie_id_bcb30ef4_fk_halls_movie_hall_id` FOREIGN KEY (`movie_id`) REFERENCES `halls_movie_hall` (`id`),
  ADD CONSTRAINT `halls_ticket_user_id_fdc40588_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
