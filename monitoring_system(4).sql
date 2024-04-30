-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 30, 2024 at 07:54 AM
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
(1, 'test', 'kolkata', '8520852020', 'test@email.com', 1, 1, '2024-04-29 15:46:26', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `md_device`
--

CREATE TABLE `md_device` (
  `device_id` bigint NOT NULL,
  `client_id` int NOT NULL,
  `device` varchar(155) NOT NULL,
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

INSERT INTO `md_device` (`device_id`, `client_id`, `device`, `do_channel`, `model`, `lat`, `lon`, `imei_no`, `last_maintenance`, `created_at`, `updated_at`) VALUES
(1, 1, 'IB00000001', 1, 'ABCDX0000', '34567890.990', '4567890.9754', 'HGGHVVJ356FG', NULL, '2024-04-29 16:11:28', NULL),
(2, 1, 'IB00000002', 1, 'ABCDX0020', '34567880.990', '4567897.9754', 'HGGHFVVJ356FG', NULL, '2024-04-29 16:16:33', NULL);

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
(1, 1, 'Organization1', 1, '2024-04-29 15:49:43', '2024-04-29 15:50:16');

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
  `create_by` int NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
);

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
  `alert_type` enum('H','L','CL','CH') DEFAULT NULL,
  `alert_status` enum('N','Y') NOT NULL DEFAULT 'N',
  `alert_value` decimal(10,2) NOT NULL,
  `alert_email` varchar(155) NOT NULL,
  `create_by` int NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
);

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
  `device_output_current` decimal(10,2) NOT NULL DEFAULT '0.00',
  `device_settings_freq` decimal(10,2) NOT NULL DEFAULT '0.00',
  `device_running_freq` decimal(10,2) NOT NULL DEFAULT '0.00',
  `device_rpm` decimal(10,2) NOT NULL DEFAULT '0.00',
  `device_flow` decimal(10,2) NOT NULL DEFAULT '0.00',
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
);

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
(21, 'PARTHA', 'partha@email.com', 1, 'Y', 'C', 585004, 'N', '$2b$12$daoApXNYu5py8wxYFiwNc.arZgmYS04hPiL4tnmD7YqwmgbOrTIUq', 0, '2024-04-03 15:36:12', NULL),
(23, 'user1', 'user1@email.com', 1, 'Y', 'U', 24181, 'N', '$2b$12$0i2DpxusvNLhEAKEy0Ln9.NdTkwDgFfMTZMHXTusrMkXYjDE9UWhy', 0, '2024-04-29 15:52:59', NULL);

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
  MODIFY `device_id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `md_manage_user_device`
--
ALTER TABLE `md_manage_user_device`
  MODIFY `manage_user_device_id` bigint NOT NULL AUTO_INCREMENT;

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
  MODIFY `unit_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `td_alert`
--
ALTER TABLE `td_alert`
  MODIFY `alert_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `td_energy_data`
--
ALTER TABLE `td_energy_data`
  MODIFY `energy_data_id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `td_ups_data`
--
ALTER TABLE `td_ups_data`
  MODIFY `ups_data_id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
