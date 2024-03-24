# MD5Checker
A tool to generate md5 of file and checkout

## MD5 Generator And Checker

### Introduction

- With this tool, you can generate MD5 from a file and check whether its MD5 is the same as the official one.
- Content:
  - [md5_checker.py](md5_checker.py)
  - [md5_checker_ui.py](md5_checker_ui.py)
  - [md5_checker_ui.ui](md5_checker_ui.ui)

### Requirements

- **sys**
- **hashlib**
- **PyQt6**

### Instruction

- Run [md5-checker.exe](md5-checker.exe)

- Click `选择文件`(Choose File) button to choose the file to be checked out and it will generate automatically the MD5 of the file

- Click `复  制`(Copy) button to copy the MD5 value of the file if you want

- Paste the **official MD5** into the `目标MD5` **textbox**

- Click `校  验`(Check) button to check whether the MD5 of chosen file is the same as the official one

- Ps. you can try it out that the correct MD5 of [md5-checker.exe](md5-checker.exe) is **7299c5c93f3c169856995213ff44a0fc**

### Statement

- **ONLY** for personal learning, **NOT for Commercial Use**!

## MD5生成校验器

### 简介

- 使用该程序生成文件MD5值，并校验是否与提供的目标MD5一致
- 包含：
  - [md5_checker.py](md5_checker.py)
  - [md5_checker_ui.py](md5_checker_ui.py)
  - [md5_checker_ui.ui](md5_checker_ui.ui)

### 需要的包

- **sys**
- **hashlib**
- **PyQt6**

### 使用说明

- 运行[md5-checker.exe](md5-checker.exe)

- 点击`选择文件`按钮选择需要生成MD5值的文件，MD5会自动显示在`文件MD5`文本框内

- 点击`复  制`按钮可以复制文件MD5值

- 将官方提供的MD5粘贴到`目标MD5`文本框

- 点击`校  验`按钮检查`文件MD5`和`目标MD5`是否一致

- Ps.可以尝试一下校验[md5-checker.exe](md5-checker.exe)的MD5值是不是**7299c5c93f3c169856995213ff44a0fc**

### 声明

- 仅供个人学习使用，**禁止商用**！
