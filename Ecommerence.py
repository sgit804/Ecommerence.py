@@ -1,13 +1,18 @@
<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

	<title>Order Info Page</title>
</head>
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
{% load staticfiles %}
	<!-- The line above tells Django to be ready to listen for static files -->
<!-- <link rel="stylesheet" href="{% static 'dashboard/css/style.css' %}"media="screen" title="no title"  charset="utf-8"> -->
<link rel="stylesheet" href="http://www.w3schools.com/lib/w3.css">
<title>Order Info Page</title>
<style>
/*	top nav bar standard!!!!!!!!!!*/
	*{
@@ -43,37 +48,190 @@
}
/*^^^top nav bar standard!!!!!!!!!^^^^^^^^*/
/*Table!!!!!!!!*/
table, tr, td{
/*table, tr, td{
	text-align: left;
	/*margin-top: 30px;*/
	margin: auto;
	/*margin: auto;
	margin-top: 30px;
	width: 900px;
	width: 900px;*/
	/*margin-left: 350px*/;


* {
	margin:0px;
	padding: 0px;
}
.icon {
	display: inline-block;
	margin-left: 15px;
}

	#wrapper {
		padding:20px;
		width: 1112px;
		height:1000px;
		margin:0px auto;
	}
/*	top nav bar standard!!!!!!!!!!*/
	#top_nav {
		padding: 5px;
		background-color: #262626;
		width: 100%;
		border-radius: 15px;
	}
	#left_table #s_bar {
		display: inline;
	}
	#s_bar {
		height: 30px;
		width: 30px;
	}
#Gzone, #S_cart {
	display: inline-block;
	color:#ffffff;
	margin-left: 15px;
}
p {
#s_cart{
	margin-left: 755px;
	color: #ffffff;
}
#ser_bar {
	opacity: 0.3;
}
/*^^^top nav bar standard!!!!!!!!!^^^^^^^^*/
#left_table {
	display: inline-block;
	padding: 10px;
	height: 250px;
	width: 250px;
	vertical-align: top;
	margin-top: 20px;
	border-radius: 10px;
	border:2px solid black;
}
#item_list {
	list-style: none;
	font-size: 20px;
}
#right_table {
	display: inline-block;
	border:2px solid;
	height: auto;
	width: 800px;
	vertical-align: top;
	margin-left: 15px;
	margin-top: 20px;
	padding-left: 20px;
	border-radius: 10px;
}
 #page_list li {
	display: inline-block;
	list-style: none;
	margin-left: 10px;
}
#right_table h2, #page_list {
	display: inline-block;
	margin-left: 10px;
}
#page_list2 li{
	display: inline;
	list-style: none;
}
.product{
  display: inline-block;
  margin-left: 10px;
  margin-right: 10px;
  vertical-align: top;
}
.product img{
  height:200px;
  width: 200px;
  border-radius: 10px;
  border: 1px solid black;
}
.product p{
  text-align: center;
}
.r1 {
	display: inline;
	height: 40px;
	width: 40px;
	background-color: red;
}
.r2 {
	display: inline;
	height: 40px;
	width: 40px;
	background-color: blue;
}
.r3 {
	display: inline;
	height: 40px;
	width: 40px;
	background-color: green;
}
ul.pagination {
	margin:380px 0px 0px 230px;
    display: inline-block;

}
ul.pagination li {
	display: inline;
}
.pagination{
  vertical-align: top;
  display: block;
}
.headermenu{
  display:block;
}
#s_cart a{
  text-decoration: none;
  color: white;
	margin-left: 125px;
}

.table_order {
	width: 700px;
	margin-left: 175px;
	margin-top: 75px;

}
</style>
</head>




<body>

<div id="wrapper">
<!-- <div id="wrapper">
		<div id="top_nav">
	<h2 id="Gzone">Granny Zone</h2><span id="s_cart">Shopping Cart ({{cartcount}})</span>
</div> -->
<div id="wrapper">
<div id="top_nav">
	<div class="icon">
		<img src="{{MEDIA_URL}}/photos/Grandma_white.png" alt="" height="60" width="60"/>
	</div>
	<h2 id="Gzone">Granny Zone</h2>
	<span id="s_cart"><a href="/checkout">Shopping Cart ({{cartcount}})</a></span>
</div>


<!-- Table!!!!!!!!!!!! -->
<div class="table_order">

<table border="1px">

<table class="table table-striped">
	<thead>
	<tr>
		<th>Item</th>
		<th>Price</th>
		<th>Quantity</th>
		<th>Total</th>
	</tr>
</thead>
<tbody>
  {%for product in products%}
	<tr>
		<td>{{product.name}}</td>
@@ -89,12 +247,16 @@ <h2 id="Gzone">Granny Zone</h2><span id="s_cart">Shopping Cart ({{cartcount}})</
	</tr>

  {%endfor%}

</tbody>
</table>
</div>

<br><br>
<a href="/deletecart">Empty Cart</a>
	<div id="keep_shopping">
	<p style="margin: 20px 0px 0px 930px;"><b>Total:</b>${{total}}</p>
	<button style="margin: 20px 0px 0px 860px;"><a href="/">Continue Shopping</a></button>
	<button class="w3-btn w3-blue-grey" style="margin: 20px 0px 0px 860px;"><a href="/">Continue Shopping</a></button>

	</div>


@@ -132,5 +294,6 @@ <h2>Billing Information</h2>
    </div>
</form>
</div>
</div>
</body>
</html>