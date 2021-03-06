#!/usr/bin/env bash

PKG=''
SYS=''
VER=''

check_system(){
    OS=`uname -s`
    if [ ${OS} == "Darwin"  ];then
        PKG='brew'
        SYS='mac'
    elif [ ${OS} == "Linux"  ];then
        source /etc/os-release
        case $ID in
            debian|ubuntu|devuan)
                PKG='apt'
                SYS='ubuntu'
                VER=${VERSION_ID}
                ;;
            centos|fedora|rhel)
                PKG="yum"
                SYS="centos"
                # if test "$(echo "$VERSION_ID >= 22" | bc)" -ne 0;
                # then
                    # PKG="dnf"
                # fi
                ;;
            *)
                exit 1
                ;;
        esac
    else
        echo "Other OS: ${OS}"
    fi
}

install(){
    echo ${SYS} ${VER}
    if [ ${SYS} == 'ubuntu' ]
    then
        if [ ${VER} == '14.04' ]
        then
            install_ubuntu1404
        elif [ ${VER} == '16.04' ]
        then
            install_ubuntu1604
        fi
    elif [ ${SYS} == 'centos' ]
    then
        install_centos7
    elif [ ${SYS} == 'mac' ]
    then
        echo ${SYS}

    fi
}


install_centos7(){
    sudo yum install -y yum-utils device-mapper-persistent-data lvm2
    sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
    sudo yum install -y docker-ce
    sudo systemctl start docker
    sudo systemctl enable docker
}

install_ubuntu1604(){
    sudo apt-get -y update
    sudo apt-get -y install \
        apt-transport-https \
        ca-certificates \
        curl \
        software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) \
        stable"
    sudo apt-get -y update
    sudo apt-get -y install docker-ce
}

install_ubuntu1404(){
    sudo apt-get -y update
    sudo apt-get -y install  linux-image-extra-$(uname -r) linux-image-extra-virtual
    sudo apt-get -y update
    sudo apt-get -y install \
        apt-transport-https \
        ca-certificates \
        curl \
        software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) \
        stable"
    sudo apt-get -y update
    sudo apt-get -y install docker-ce
}

check_system
install
echo ${VER} ${SYS}
