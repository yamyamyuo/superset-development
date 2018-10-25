#!/bin/bash
current_dir=$(cd $(dirname $0);pwd)

# 1. cd incubator-superset project
SUPERSET_ROOT_DIR="/Users/serena/Downloads/incubator-superset-0.26.2-clean"

# 2. move conf and security dir to your superset source code root dir
# 首先将该目录下的 conf 和 security 分别复制到superset 源码的根目录下
cp -r $current_dir/../conf $SUPERSET_ROOT_DIR
cp -r $current_dir/../security $SUPERSET_ROOT_DIR

# 3. you should export some environment variable
export SUPERSET_CONFIG_PATH="$SUPERSET_ROOT_DIR/conf/superset_config.py"
export PYTHONPATH=$SUPERSET_ROOT_DIR

# 4. copy the login html to superset frontend html templates directory
# 将我们自己写的登录页面放到superset的前端模板目录下
SUPERSET_TEMPLATES_DIR="$SUPERSET_ROOT_DIR/superset/templates/appbuilder/general"
SUPERSET_SECURITY_TEMPLATE_DIR="$SUPERSET_TEMPLATES_DIR/security"
mkdir $SUPERSET_SECURITY_TEMPLATE_DIR
cp $current_dir/../security/login_my.html $SUPERSET_SECURITY_TEMPLATE_DIR

# 5. run the following command to start superset server
# 通过bash sbin/start_conf_script.sh 之后, 跑到你的superset 项目执行一下命令
# cd your_superset_code_root
# python superset/bin/superset runserver -d
# 输入 Admin@example.com, 密码随意, 即可完成登录