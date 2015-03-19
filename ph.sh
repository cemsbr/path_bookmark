#!/bin/bash

alias h='~/.path_hash/ph.py'
alias hl='h ls'
alias ha='h add'
alias hr='h rm'
alias hcd='he cd'

function he() {
    cmd=$(h exec "$@")
    eval "$cmd"
}

_ph() {
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    opts=$(h keys)
    COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
    return 0
}

_ph_eq() {
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    _get_comp_words_by_ref -n = cur
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    if [ "${cur::1}" == '=' ]; then
      opts=$(h keys)
      COMPREPLY=( $(compgen -W "${opts}" -- ${cur:1}) )
    else
      COMPREPLY=( $(compgen -f  -- "${COMP_WORDS[${COMP_CWORD}]}" ) )
    fi
    return 0
}

complete -F _ph hr
complete -F _ph_eq he
complete -F _ph_eq hcd
