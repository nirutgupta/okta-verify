# generates google auth OTP
generate_otp () {
  cmd_output=$(echo "$1"| authenticator generate --refresh "once")
  set -- $cmd_output
  auth_code=$4
  echo "$auth_code"
}

# used to check stats
is_vpn_connected () {
  /opt/cisco/anyconnect/bin/vpn stats
}

# connects to vpn
connect_to_vpn(){
echo "$1
$2
$3
$4
$5
$6
$7
$8" | /opt/cisco/anyconnect/bin/vpn -s connect connect.cloudera.com
}

# disconnects from vpn
disconnect_from_vpn(){
  /opt/cisco/anyconnect/bin/vpn disconnect
}


otp=$( generate_otp "nirutgupta" )
if [[ $otp =~ ^[0-9]{6}$ ]]
then
  echo "Valid OTP"
else
  echo "Invalid OTP! Passphrase is incorrect"
fi

connect_to_vpn "<vpn name>" "<user name>" "<password>" "y" "3" "y" "$otp" "y"
say VPN Connected
#sleep 10
#disconnect_from_vpn
