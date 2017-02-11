<!DOCTYPE html>
<html>
  <head>
    <title> BotMan's BoothMultiplier </title>

    <!-- The beautifying framework files  -->
    <link rel="stylesheet" href="static/css/bootstrap.min.css">
    <script src="static/js/jquery-3.0.0.min.js" charset="utf-8"></script>
    <script src="static/js/bootstrap.min.js" charset="utf-8"></script>

    <!-- This is required to make the page responsive for mobile devices -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

  </head>

  <body>
    <header class="jumbotron text-center"
            style="background-color: #00695C; color: white;">
      <h1> <b> Booth Multiplier </b> </h1>
    </header>

    <main>
      <div class="container">
        % include("MultiplyNumbersForm")

        % if(defined("ans")):
          % include("ResultDisplay", answer=ans)
        % else:
          % pass
      </div>
    </main>

  </body>
</html>
