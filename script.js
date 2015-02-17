// My script
// short hand for $(document).ready(function(){
$(function(){
    $("a").addClass("aBold");
    $("a").click(function(event){
	// alert("baby come back!");
	$(this).hide(1000);
	event.preventDefault();
	console.log("i won't let you leave!!");
    });
});
