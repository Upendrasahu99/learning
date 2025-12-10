import { GoogleLogin } from "@react-oauth/google";

function GoogleLoginComponent() {
  const handleGoogleSuccess = (credentialResponse :any) => {
    console.log(credentialResponse); // Send this to backend////////////////
  };


  return (
    <div className="w-full flex justify-center my-4 rounded-lg">
      <GoogleLogin
        onSuccess={handleGoogleSuccess}
        onError={() => console.log("Login Failed")}

        width="280"

      />
    </div>
  );
}

export default GoogleLoginComponent;