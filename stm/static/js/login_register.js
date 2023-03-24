$("document").ready(function(){
  $("#SignInbtn").on("click",       function() {
    $(".signUpForm").addClass('hidden');
    $(".signInForm").removeClass('hidden');
        $(".signUpForm").removeClass('fadein');
    $(".signInForm").addClass('fadein');
    $(".signInText").addClass('hidden');
    $(".signUpText").removeClass('hidden');
    $(".login-section h1").text("sign-in NLP ACCOUNT");
  })
  $("#SignUpbtn").on("click",function() {
    debugger;
    $(".signInForm").addClass('hidden');
    $(".signUpForm").removeClass('hidden');
           $(".signInForm").removeClass('fadein');
    $(".signUpForm").addClass('fadein');
    $(".signUpText").addClass('hidden');
    $(".signInText").removeClass('hidden');
    $(".login-section h1").text("SignUp NLP ACCOUNT");
  })
})