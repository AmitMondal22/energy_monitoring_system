-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 02, 2024 at 05:04 PM
-- Server version: 8.0.36-0ubuntu0.22.04.1
-- PHP Version: 8.1.2-1ubuntu2.14

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
  `user_name` varchar(155) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `user_email` varchar(155) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `user_info_id` varchar(155) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `user_active_status` enum('Y','N') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `user_type` enum('S','A','C','U') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'S=super admin, a=admin, c=company, U=user',
  `otp_number` int NOT NULL DEFAULT '0',
  `otp_active_status` enum('N','Y') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(155) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_by` int NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `del_users`
--

INSERT INTO `del_users` (`user_id`, `user_name`, `user_email`, `user_info_id`, `user_active_status`, `user_type`, `otp_number`, `otp_active_status`, `password`, `created_by`, `created_at`, `updated_at`) VALUES
(18, 'test user', 'hjgjhg@jhgbk', '1', 'Y', 'U', 989484, 'N', '$2b$12$oItsDdmLHXxaZANA6AW7zuQXIzWk6.nOKorAZ5zThKNJdYL.5ZPIm', 0, '2024-04-01 07:32:41', '2024-04-01 09:44:04');

-- --------------------------------------------------------

--
-- Table structure for table `md_device`
--

CREATE TABLE `md_device` (
  `device_id` bigint NOT NULL,
  `device` varchar(155) NOT NULL,
  `do_channel` int NOT NULL,
  `model` varchar(155) NOT NULL,
  `lat` varchar(50) NOT NULL,
  `lon` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `imei_no` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `last_maintenance` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `md_device`
--

INSERT INTO `md_device` (`device_id`, `device`, `do_channel`, `model`, `lat`, `lon`, `imei_no`, `last_maintenance`, `created_at`, `updated_at`) VALUES
(1, 'IB00000001', 3, 'rtg435', '46426', '462345', '3245466', NULL, '2024-04-02 09:45:40', NULL),
(2, 'IB00000002', 3, 'rtg435', '46426', '462345', '324546', NULL, '2024-04-02 09:47:25', NULL),
(3, 'IB00000003', 3, 'rtg435', '46426', '462345', '32454689', NULL, '2024-04-02 09:49:37', NULL),
(4, 'IB00000004', 3, 'rtg435', '46426', '462345', '324564689', NULL, '2024-04-02 09:51:06', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `md_manage_user_device`
--

CREATE TABLE `md_manage_user_device` (
  `manage_user_device_id` bigint NOT NULL,
  `organization_id` int NOT NULL,
  `user_id` int NOT NULL,
  `device_id` int NOT NULL,
  `created_by` int NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `md_organization`
--

CREATE TABLE `md_organization` (
  `organization_id` bigint NOT NULL,
  `organization_name` varchar(155) NOT NULL,
  `created_by` int NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `md_organization`
--

INSERT INTO `md_organization` (`organization_id`, `organization_name`, `created_by`, `created_at`, `updated_at`) VALUES
(1, 'test2', 1, '2024-04-01 09:36:48', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `md_super_admin`
--

CREATE TABLE `md_super_admin` (
  `super_admin_id` int NOT NULL,
  `name` varchar(155) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(155) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `mobile_number` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '0',
  `address` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `created_by` int NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `td_energy_data`
--

CREATE TABLE `td_energy_data` (
  `energy_data_id` bigint NOT NULL,
  `device_id` bigint NOT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` bigint NOT NULL,
  `user_name` varchar(155) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `user_email` varchar(155) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `user_info_id` varchar(155) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `user_active_status` enum('Y','N') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `user_type` enum('S','A','C','U') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'S=super admin, a=admin, c=company, U=user',
  `otp_number` int NOT NULL DEFAULT '0',
  `otp_active_status` enum('N','Y') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(155) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_by` int NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `user_name`, `user_email`, `user_info_id`, `user_active_status`, `user_type`, `otp_number`, `otp_active_status`, `password`, `created_by`, `created_at`, `updated_at`) VALUES
(16, 'Amit Mondal', 'amit@iotblitz.com', '1', 'Y', 'S', 197840, 'N', '$2b$12$daoApXNYu5py8wxYFiwNc.arZgmYS04hPiL4tnmD7YqwmgbOrTIUq', 0, '2024-03-27 11:28:35', NULL),
(17, 'test', 'abc@jkhjk.fv', '1', 'Y', 'A', 356535, 'N', '$2b$12$NnD4fOsjeRgCNPHp.mS73uk4Jvt6dtMSepTg9Lx3eg51Aewc5r.va', 0, '2024-03-29 07:28:01', NULL),
(20, 'hello', 'hgydyt@suo.uyt', '1', 'Y', 'U', 859093, 'N', '$2b$12$XvbjGoMdjfT7KVJK.VBCUeU/jRUiyQJbRL6V7CwI6s59gL0YaYSX6', 0, '2024-04-01 09:53:37', NULL);

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
-- Indexes for table `md_device`
--
ALTER TABLE `md_device`
  ADD PRIMARY KEY (`device_id`),
  ADD UNIQUE KEY `device` (`device`,`imei_no`);

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
-- Indexes for table `td_energy_data`
--
ALTER TABLE `td_energy_data`
  ADD PRIMARY KEY (`energy_data_id`);

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
  MODIFY `user_id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `md_device`
--
ALTER TABLE `md_device`
  MODIFY `device_id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `md_manage_user_device`
--
ALTER TABLE `md_manage_user_device`
  MODIFY `manage_user_device_id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `md_organization`
--
ALTER TABLE `md_organization`
  MODIFY `organization_id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `md_super_admin`
--
ALTER TABLE `md_super_admin`
  MODIFY `super_admin_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `td_energy_data`
--
ALTER TABLE `td_energy_data`
  MODIFY `energy_data_id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
