{ pkgs ? import <nixpkgs> {}}:
with pkgs;
with python3Packages;
buildPythonPackage {
	name = "template";
	src = nix/local.tgz;
	buildInputs = [jinja2];
}
