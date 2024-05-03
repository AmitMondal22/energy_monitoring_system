-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 03, 2024 at 08:17 AM
-- Server version: 8.0.36-0ubuntu0.22.04.1
-- PHP Version: 8.1.2-1ubuntu2.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `monitoring_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `del_users`
--

CREATE TABLE `del_users` (
  `user_id` bigint NOT NULL,
  `user_name` varchar(155) NOT NULL,
  `user_email` varchar(155) NOT NULL,
  `user_info_id` varchar(155) NOT NULL,
  `user_active_status` enum('Y','N') NOT NULL,
  `user_type` enum('S','A','C','U') NOT NULL COMMENT 'S=super admin, a=admin, c=company, U=user',
  `otp_number` int NOT NULL DEFAULT '0',
  `otp_active_status` enum('N','Y') NOT NULL,
  `password` varchar(155) NOT NULL,
  `created_by` int NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
);

-- --------------------------------------------------------

--
-- Table structure for table `md_assign_customer_device`
--

CREATE TABLE `md_assign_customer_device` (
  `assign_customer_device_id` int NOT NULL,
  `device_id` int NOT NULL,
  `device` varchar(155) NOT NULL,
  `client_id` int NOT NULL,
  `created_by` int NOT NULL,
  `updated_by` int DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
);

-- --------------------------------------------------------

--
-- Table structure for table `md_client`
--

CREATE TABLE `md_client` (
  `client_id` int NOT NULL,
  `client_name` varchar(255) NOT NULL,
  `client_address` text NOT NULL,
  `client_mobile` varchar(20) NOT NULL,
  `client_email` varchar(155) NOT NULL,
  `create_by` int NOT NULL,
  `updated_by` int DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
);

--
-- Dumping data for table `md_client`
--

INSERT INTO `md_client` (`client_id`, `client_name`, `client_address`, `client_mobile`, `client_email`, `create_by`, `updated_by`, `created_at`, `updated_at`) VALUES
(1, 'RAJARAM', 'KOLKATA', '7890833920', 'snc@email.com', 1, NULL, '2024-04-30 05:21:21', '2024-04-30 05:21:21');

-- --------------------------------------------------------

--
-- Table structure for table `md_device`
--

CREATE TABLE `md_device` (
  `device_id` bigint NOT NULL,
  `client_id` int NOT NULL,
  `device` varchar(155) NOT NULL,
  `device_name` varchar(155) DEFAULT NULL,
  `do_channel` int NOT NULL,
  `model` varchar(155) NOT NULL,
  `lat` varchar(50) NOT NULL,
  `lon` varchar(50) NOT NULL,
  `imei_no` varchar(80) NOT NULL,
  `last_maintenance` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
);

--
-- Dumping data for table `md_device`
--

INSERT INTO `md_device` (`device_id`, `client_id`, `device`, `device_name`, `do_channel`, `model`, `lat`, `lon`, `imei_no`, `last_maintenance`, `created_at`, `updated_at`) VALUES
(1, 1, '123456789', '', 1, '123456789', '123456789.54', '123456789.54', '123456789IMEI', '2024-04-30 05:46:21', '2024-04-30 05:46:21', '2024-04-30 05:46:21'),
(2, 1, 'dfwsedc', 'wedcdew', 2, 'dawscaw', 'w2321312', '123213', 'df233r23', '2024-04-29 18:30:00', '2024-04-30 09:42:56', '2024-04-30 10:23:49'),
(7, 1, '1234567891', 'abc', 1, 'uioyouo', '647.87', '4864.78', 'gy556n7345555', '2024-04-29 18:30:00', '2024-04-30 10:04:11', NULL),
(8, 1, '1234567892', 'abc', 1, 'uioyouo', '647.87', '4864.78', 'gyutu556345555', '2024-04-29 18:30:00', '2024-04-30 10:04:11', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `md_manage_user_device`
--

CREATE TABLE `md_manage_user_device` (
  `manage_user_device_id` bigint NOT NULL,
  `client_id` int NOT NULL,
  `organization_id` int NOT NULL,
  `user_id` int NOT NULL,
  `device_id` int NOT NULL,
  `device` varchar(155) NOT NULL,
  `created_by` int NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
);

--
-- Dumping data for table `md_manage_user_device`
--

INSERT INTO `md_manage_user_device` (`manage_user_device_id`, `client_id`, `organization_id`, `user_id`, `device_id`, `device`, `created_by`, `created_at`, `updated_at`) VALUES
(1, 1, 1, 2, 1, '123456789', 1, '2024-04-30 05:45:39', '2024-04-30 06:20:29');

-- --------------------------------------------------------

--
-- Table structure for table `md_organization`
--

CREATE TABLE `md_organization` (
  `organization_id` bigint NOT NULL,
  `client_id` int NOT NULL,
  `organization_name` varchar(155) NOT NULL,
  `created_by` int NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
);

--
-- Dumping data for table `md_organization`
--

INSERT INTO `md_organization` (`organization_id`, `client_id`, `organization_name`, `created_by`, `created_at`, `updated_at`) VALUES
(1, 1, 'organization name', 0, '2024-04-30 05:23:45', '2024-04-30 05:26:08');

-- --------------------------------------------------------

--
-- Table structure for table `md_super_admin`
--

CREATE TABLE `md_super_admin` (
  `super_admin_id` int NOT NULL,
  `name` varchar(155) NOT NULL,
  `email` varchar(155) NOT NULL,
  `mobile_number` varchar(20) NOT NULL DEFAULT '0',
  `address` text,
  `created_by` int NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
);

-- --------------------------------------------------------

--
-- Table structure for table `md_unit`
--

CREATE TABLE `md_unit` (
  `unit_id` int NOT NULL,
  `unit` varchar(155) NOT NULL,
  `unit_name` varchar(155) NOT NULL,
  `create_by` int NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
);

--
-- Dumping data for table `md_unit`
--

INSERT INTO `md_unit` (`unit_id`, `unit`, `unit_name`, `create_by`, `created_at`, `updated_at`) VALUES
(1, 'device_dc_bus_voltage', 'device dc bus voltage', 1, '2024-04-30 06:57:50', '2024-04-30 06:57:50');

-- --------------------------------------------------------

--
-- Table structure for table `td_alert`
--

CREATE TABLE `td_alert` (
  `alert_id` int NOT NULL,
  `client_id` int NOT NULL,
  `organization_id` int NOT NULL,
  `device_id` int NOT NULL,
  `device` varchar(50) NOT NULL,
  `unit_id` int NOT NULL,
  `alert_type` enum('1CL','2L','3H','4CH') DEFAULT NULL,
  `alert_status` enum('N','Y') NOT NULL DEFAULT 'N',
  `alert_value` decimal(10,2) NOT NULL,
  `alert_email` varchar(155) NOT NULL,
  `create_by` int NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
);

--
-- Dumping data for table `td_alert`
--

INSERT INTO `td_alert` (`alert_id`, `client_id`, `organization_id`, `device_id`, `device`, `unit_id`, `alert_type`, `alert_status`, `alert_value`, `alert_email`, `create_by`, `created_at`, `updated_at`) VALUES
(1, 1, 1, 1, '123456789', 1, '2L', 'Y', '20.00', 'abc2email.com', 2, '2024-05-02 10:06:58', '2024-05-02 10:06:58'),
(5, 1, 1, 1, '123456789', 1, '1CL', 'Y', '10.00', 'abc2email.com', 2, '2024-05-02 10:06:58', '2024-05-02 10:06:58'),
(6, 1, 1, 1, '123456789', 1, '3H', 'Y', '30.00', 'abc2email.com', 2, '2024-05-02 10:06:58', '2024-05-02 10:06:58');

-- --------------------------------------------------------

--
-- Table structure for table `td_energy_data`
--

CREATE TABLE `td_energy_data` (
  `energy_data_id` bigint NOT NULL,
  `client_id` int NOT NULL,
  `device_id` int NOT NULL,
  `device` varchar(155) NOT NULL,
  `do_channel` int NOT NULL,
  `device_run_hours` int NOT NULL,
  `device_dc_bus_voltage` decimal(10,2) NOT NULL DEFAULT '0.00',
  `device_dc_bus_voltage2` decimal(10,2) NOT NULL,
  `device_dc_bus_voltage3` decimal(10,2) NOT NULL,
  `device_output_current` decimal(10,2) NOT NULL DEFAULT '0.00',
  `device_output_current2` decimal(10,2) NOT NULL,
  `device_output_current3` decimal(10,2) NOT NULL,
  `device_settings_freq` decimal(10,2) NOT NULL DEFAULT '0.00',
  `device_running_freq` decimal(10,2) NOT NULL DEFAULT '0.00',
  `device_rpm` decimal(10,2) NOT NULL DEFAULT '0.00',
  `device_flow` decimal(10,2) NOT NULL DEFAULT '0.00',
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
);

--
-- Dumping data for table `td_energy_data`
--

INSERT INTO `td_energy_data` (`energy_data_id`, `client_id`, `device_id`, `device`, `do_channel`, `device_run_hours`, `device_dc_bus_voltage`, `device_dc_bus_voltage2`, `device_dc_bus_voltage3`, `device_output_current`, `device_output_current2`, `device_output_current3`, `device_settings_freq`, `device_running_freq`, `device_rpm`, `device_flow`, `date`, `time`, `created_at`, `updated_at`) VALUES
(1, 1, 1, '123456789', 1, 10, '12.00', '0.00', '0.00', '45.00', '0.00', '0.00', '52.00', '46.00', '50.00', '56.00', '2024-04-30', '18:17:40', '2024-04-30 12:47:40', NULL),
(2, 1, 1, '123456789', 1, 10, '12.00', '0.00', '0.00', '45.00', '0.00', '0.00', '52.00', '46.00', '50.00', '56.00', '2024-04-30', '18:19:35', '2024-04-30 12:49:35', NULL),
(3, 1, 1, '123456789', 1, 10, '12.00', '0.00', '0.00', '45.00', '0.00', '0.00', '52.00', '46.00', '50.00', '56.00', '2024-04-30', '18:19:51', '2024-04-30 12:49:51', NULL),
(4, 1, 1, '123456789', 1, 10, '12.00', '0.00', '0.00', '45.00', '0.00', '0.00', '52.00', '46.00', '50.00', '56.00', '2024-04-30', '18:20:15', '2024-04-30 12:50:15', NULL),
(5, 1, 1, '123456789', 1, 10, '12.00', '0.00', '0.00', '45.00', '0.00', '0.00', '52.00', '46.00', '50.00', '56.00', '2024-04-30', '18:20:34', '2024-04-30 12:50:34', NULL),
(6, 1, 1, '123456789', 1, 10, '12.00', '0.00', '0.00', '45.00', '0.00', '0.00', '52.00', '46.00', '50.00', '56.00', '2024-04-30', '18:45:03', '2024-04-30 13:15:03', NULL),
(7, 1, 1, '123456789', 1, 10, '12.00', '0.00', '0.00', '45.00', '0.00', '0.00', '52.00', '46.00', '50.00', '56.00', '2024-04-30', '19:09:17', '2024-04-30 13:39:17', NULL),
(8, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '11:13:31', '2024-05-02 05:43:31', NULL),
(9, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '11:19:06', '2024-05-02 05:49:06', NULL),
(10, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '13:21:10', '2024-05-02 07:51:10', NULL),
(11, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '13:25:52', '2024-05-02 07:55:52', NULL),
(12, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '13:28:30', '2024-05-02 07:58:30', NULL),
(13, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '13:30:11', '2024-05-02 08:00:11', NULL),
(14, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '13:31:14', '2024-05-02 08:01:14', NULL),
(15, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '13:31:19', '2024-05-02 08:01:19', NULL),
(16, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '13:31:36', '2024-05-02 08:01:36', NULL),
(17, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '13:31:45', '2024-05-02 08:01:45', NULL),
(18, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '13:33:26', '2024-05-02 08:03:26', NULL),
(19, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '13:34:44', '2024-05-02 08:04:44', NULL),
(20, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '13:35:59', '2024-05-02 08:05:59', NULL),
(21, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '15:13:09', '2024-05-02 09:43:09', NULL),
(22, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '15:13:40', '2024-05-02 09:43:40', NULL),
(23, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '15:13:58', '2024-05-02 09:43:58', NULL),
(24, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '15:36:40', '2024-05-02 10:06:40', NULL),
(25, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '15:39:11', '2024-05-02 10:09:11', NULL),
(26, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '15:39:50', '2024-05-02 10:09:50', NULL),
(27, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '15:39:57', '2024-05-02 10:09:57', NULL),
(28, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '15:40:29', '2024-05-02 10:10:29', NULL),
(29, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '15:41:10', '2024-05-02 10:11:10', NULL),
(30, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '15:43:33', '2024-05-02 10:13:33', NULL),
(31, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '15:44:49', '2024-05-02 10:14:49', NULL),
(32, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '15:45:27', '2024-05-02 10:15:27', NULL),
(33, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '15:50:24', '2024-05-02 10:20:24', NULL),
(34, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '15:50:51', '2024-05-02 10:20:51', NULL),
(35, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '15:51:09', '2024-05-02 10:21:09', NULL),
(36, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '16:05:42', '2024-05-02 10:35:42', NULL),
(37, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '16:07:16', '2024-05-02 10:37:16', NULL),
(38, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '16:08:05', '2024-05-02 10:38:05', NULL),
(39, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '16:08:46', '2024-05-02 10:38:46', NULL),
(40, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '16:09:56', '2024-05-02 10:39:56', NULL),
(41, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '16:10:33', '2024-05-02 10:40:33', NULL),
(42, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '16:13:58', '2024-05-02 10:43:58', NULL),
(43, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '16:15:51', '2024-05-02 10:45:51', NULL),
(44, 1, 1, '123456789', 1, 2, '51.64', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '16:16:46', '2024-05-02 10:46:46', NULL),
(45, 1, 1, '123456789', 1, 2, '1.00', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '16:17:06', '2024-05-02 10:47:06', NULL),
(46, 1, 1, '123456789', 1, 2, '11.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '16:17:31', '2024-05-02 10:47:31', NULL),
(47, 1, 1, '123456789', 1, 2, '11.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '16:17:46', '2024-05-02 10:47:46', NULL),
(48, 1, 1, '123456789', 1, 2, '20.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '16:18:07', '2024-05-02 10:48:07', NULL),
(49, 1, 1, '123456789', 1, 2, '20.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '16:19:11', '2024-05-02 10:49:11', NULL),
(50, 1, 1, '123456789', 1, 2, '20.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '16:20:00', '2024-05-02 10:50:00', NULL),
(51, 1, 1, '123456789', 1, 2, '20.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '16:20:47', '2024-05-02 10:50:47', NULL),
(52, 1, 1, '123456789', 1, 2, '20.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '16:23:51', '2024-05-02 10:53:51', NULL),
(53, 1, 1, '123456789', 1, 2, '30.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '16:24:28', '2024-05-02 10:54:28', NULL),
(54, 1, 1, '123456789', 1, 2, '30.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '16:24:54', '2024-05-02 10:54:54', NULL),
(55, 1, 1, '123456789', 1, 2, '10.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '16:50:14', '2024-05-02 11:20:14', NULL),
(56, 1, 1, '123456789', 1, 2, '10.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '16:53:45', '2024-05-02 11:23:45', NULL),
(57, 1, 1, '123456789', 1, 2, '10.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '17:00:21', '2024-05-02 11:30:21', NULL),
(58, 1, 1, '123456789', 1, 2, '10.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '17:01:23', '2024-05-02 11:31:23', NULL),
(59, 1, 1, '123456789', 1, 2, '10.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '17:52:23', '2024-05-02 12:22:23', NULL),
(60, 1, 1, '123456789', 1, 2, '10.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '17:55:54', '2024-05-02 12:25:54', NULL),
(61, 1, 1, '123456789', 1, 2, '10.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '17:56:26', '2024-05-02 12:26:26', NULL),
(62, 1, 1, '123456789', 1, 2, '10.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '17:57:14', '2024-05-02 12:27:14', NULL),
(63, 1, 1, '123456789', 1, 2, '10.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '17:58:52', '2024-05-02 12:28:52', NULL),
(64, 1, 1, '123456789', 1, 2, '10.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '17:59:40', '2024-05-02 12:29:40', NULL),
(65, 1, 1, '123456789', 1, 2, '10.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '19:15:03', '2024-05-02 13:45:03', NULL),
(66, 1, 1, '123456789', 1, 2, '10.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '19:15:26', '2024-05-02 13:45:26', NULL),
(67, 1, 1, '123456789', 1, 2, '10.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '19:17:09', '2024-05-02 13:47:09', NULL),
(68, 1, 1, '123456789', 1, 2, '10.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '19:17:19', '2024-05-02 13:47:19', NULL),
(69, 1, 1, '123456789', 1, 2, '10.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '19:18:26', '2024-05-02 13:48:26', NULL),
(70, 1, 1, '123456789', 1, 2, '10.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '19:19:17', '2024-05-02 13:49:17', NULL),
(71, 1, 1, '123456789', 1, 2, '10.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '19:19:59', '2024-05-02 13:49:59', NULL),
(72, 1, 1, '123456789', 1, 2, '10.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '19:20:27', '2024-05-02 13:50:27', NULL),
(73, 1, 1, '123456789', 1, 2, '10.01', '215.46', '456.23', '7894.65', '8945.64', '48.15', '486.15', '75.16', '46.15', '1.64', '2024-05-02', '19:28:42', '2024-05-02 13:58:42', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `td_ups_data`
--

CREATE TABLE `td_ups_data` (
  `ups_data_id` bigint NOT NULL,
  `client_id` int NOT NULL,
  `device_id` int NOT NULL,
  `device` varchar(155) NOT NULL,
  `do_channel` int NOT NULL,
  `output_current` decimal(10,2) NOT NULL,
  `input_current` decimal(10,2) NOT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` bigint NOT NULL,
  `user_name` varchar(155) NOT NULL,
  `user_email` varchar(155) NOT NULL,
  `user_info_id` int NOT NULL,
  `user_active_status` enum('Y','N') NOT NULL,
  `user_type` enum('S','A','C','O','U') NOT NULL COMMENT 'S=super admin, a=admin, c=client,\r\nO=organization U=user',
  `otp_number` int NOT NULL DEFAULT '0',
  `otp_active_status` enum('N','Y') NOT NULL,
  `password` varchar(155) NOT NULL,
  `created_by` int NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
);

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `user_name`, `user_email`, `user_info_id`, `user_active_status`, `user_type`, `otp_number`, `otp_active_status`, `password`, `created_by`, `created_at`, `updated_at`) VALUES
(1, 'SNC', 'admin@snc.com', 1, 'Y', 'C', 800094, 'N', '$2b$12$39Zwv2vx3IUEpQ7g/axHLeyI68c4BvQVUl.HM3NcZS/mllLmeR2dG', 0, '2024-04-30 05:20:35', NULL),
(2, 'raja', 'raja@snc.in', 1, 'Y', 'U', 821462, 'N', '$2b$12$I58GKGvmwQ6ig21IdR1uXu2I65Loqb069/Ku1okTQsGI8xj93YnlK', 0, '2024-04-30 05:28:08', '2024-04-30 05:30:43');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `del_users`
--
ALTER TABLE `del_users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `USER_EMAIL` (`user_email`);

--
-- Indexes for table `md_assign_customer_device`
--
ALTER TABLE `md_assign_customer_device`
  ADD PRIMARY KEY (`assign_customer_device_id`);

--
-- Indexes for table `md_client`
--
ALTER TABLE `md_client`
  ADD PRIMARY KEY (`client_id`);

--
-- Indexes for table `md_device`
--
ALTER TABLE `md_device`
  ADD PRIMARY KEY (`device_id`),
  ADD UNIQUE KEY `client_id` (`client_id`,`device`,`imei_no`),
  ADD UNIQUE KEY `imei_no` (`imei_no`);

--
-- Indexes for table `md_manage_user_device`
--
ALTER TABLE `md_manage_user_device`
  ADD PRIMARY KEY (`manage_user_device_id`),
  ADD UNIQUE KEY `organization_id` (`organization_id`,`user_id`,`device_id`);

--
-- Indexes for table `md_organization`
--
ALTER TABLE `md_organization`
  ADD PRIMARY KEY (`organization_id`);

--
-- Indexes for table `md_super_admin`
--
ALTER TABLE `md_super_admin`
  ADD PRIMARY KEY (`super_admin_id`),
  ADD UNIQUE KEY `EMAIL` (`email`);

--
-- Indexes for table `md_unit`
--
ALTER TABLE `md_unit`
  ADD PRIMARY KEY (`unit_id`);

--
-- Indexes for table `td_alert`
--
ALTER TABLE `td_alert`
  ADD PRIMARY KEY (`alert_id`),
  ADD UNIQUE KEY `client_id` (`client_id`,`organization_id`,`device_id`,`device`,`unit_id`,`alert_type`);

--
-- Indexes for table `td_energy_data`
--
ALTER TABLE `td_energy_data`
  ADD PRIMARY KEY (`energy_data_id`);

--
-- Indexes for table `td_ups_data`
--
ALTER TABLE `td_ups_data`
  ADD PRIMARY KEY (`ups_data_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `USER_EMAIL` (`user_email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `del_users`
--
ALTER TABLE `del_users`
  MODIFY `user_id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `md_assign_customer_device`
--
ALTER TABLE `md_assign_customer_device`
  MODIFY `assign_customer_device_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `md_client`
--
ALTER TABLE `md_client`
  MODIFY `client_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `md_device`
--
ALTER TABLE `md_device`
  MODIFY `device_id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `md_manage_user_device`
--
ALTER TABLE `md_manage_user_device`
  MODIFY `manage_user_device_id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `md_organization`
--
ALTER TABLE `md_organization`
  MODIFY `organization_id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `md_super_admin`
--
ALTER TABLE `md_super_admin`
  MODIFY `super_admin_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `md_unit`
--
ALTER TABLE `md_unit`
  MODIFY `unit_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `td_alert`
--
ALTER TABLE `td_alert`
  MODIFY `alert_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `td_energy_data`
--
ALTER TABLE `td_energy_data`
  MODIFY `energy_data_id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=74;

--
-- AUTO_INCREMENT for table `td_ups_data`
--
ALTER TABLE `td_ups_data`
  MODIFY `ups_data_id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
