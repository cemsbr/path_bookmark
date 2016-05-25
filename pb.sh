#!/bin/bash

alias p='~/.path_bookmark/pb.py'
alias pl='p ls'
alias pa='p add'
alias pr='p rm'
alias pcd='pe cd'

function pe() {
    cmd=$(p replace "$@")
    eval "$cmd"
}

_pb() {
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    opts=$(p keys)
    COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
    return 0
}

_pb_eq() {
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    _get_comp_words_by_ref -n = cur
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    if [ "${cur::1}" == '=' ]; then
      opts=$(p keys)
      COMPREPLY=( $(compgen -W "${opts}" -- ${cur:1}) )
    else
      COMPREPLY=( $(compgen -f  -- "${COMP_WORDS[${COMP_CWORD}]}" ) )
    fi
    return 0
}

complete -F _pb pr
complete -F _pb_eq pe
complete -F _pb_eq pcd
