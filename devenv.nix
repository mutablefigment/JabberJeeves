{ pkgs, lib, config, inputs, ... }:

{
  # https://devenv.sh/basics/
  env.GREET = "devenv";

  # https://devenv.sh/packages/
  packages = [ 
    pkgs.git 
  
    # python dependencies
    pkgs.python311Packages.slixmpp
    pkgs.python311Packages.openai
    pkgs.python311Packages.duckdb
  ];

  # https://devenv.sh/scripts/
  enterShell = ''
  '';

  # https://devenv.sh/tests/
  enterTest = ''
  '';

  # https://devenv.sh/services/
  # services.postgres.enable = true;

  # https://devenv.sh/languages/
  languages.python.enable = true;

  # https://devenv.sh/pre-commit-hooks/
  pre-commit.hooks.black.enable = true;

  # https://devenv.sh/processes/
  processes.ping.exec = "./JabberJeeves.py";

  # See full reference at https://devenv.sh/reference/options/
}
