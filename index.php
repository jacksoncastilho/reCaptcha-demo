<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>reCaptcha</title>

    <script src="https://www.google.com/recaptcha/api.js" async defer></script>

</head>
<body>
    <form id="some-form" method="POST">
        <div class="g-recaptcha" data-sitekey="6LdDW-QqAAAAABAJ5lP8r1O4shPhX6gm-oz4Xx3R"></div>
        <br/>
        <button>Submit</button>
    </form>
</body>
</html>

<?php
    if($_POST) {
        echo "</br><textarea readonly style=\"width: 517px; height: 189px;\">";
        echo $_POST['g-recaptcha-response'];
        echo "</textarea>";
    
        $curl = curl_init();

        curl_setopt_array($curl, [
            CURLOPT_URL => 'https://www.google.com/recaptcha/api/siteverify',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_CUSTOMREQUEST => 'POST',
            CURLOPT_POSTFIELDS => [
                'secret' => '6LdDW-QqAAAAANlIClUlaAGv507jVQ8bAbqJtjCS',
                'response' => $_POST['g-recaptcha-response'] ?? ''
            ]
        ]);

        $response = curl_exec($curl);

        curl_close($curl);

        echo "</br></br>";
        print_r($response);
    }
?>