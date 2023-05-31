generate_otp () {
  cmd_output=$(echo "$1"| authenticator generate --refresh "once")
  set -- $cmd_output
  auth_code=$4
  echo "$auth_code"
}

otp=$( generate_otp "nirutgupta" )
echo $otp