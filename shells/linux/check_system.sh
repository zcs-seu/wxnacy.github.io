#!/usr/bin/env bash

PKG=''
SYS=''

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

    echo "${PKG}-${SYS}"
}


check_system
