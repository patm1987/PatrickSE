# Patrick SE
## Patrick Software Engineer
### Who Am I?
I'm a Senior Software Engineer at Sphero working in an internal prototyping/R&D Group.
### What Happened to PatrickSE.com?
I've been lax at maintaining my old Wordpress site during my tenure at [Sphero](http://sphero.com). I'm actively backing up my site and planning on redeploying it when I can. Until then you can check out:
* [Pux0r3.com](http://pux0r3.com) where I keep some fun side projects
* [GitHub Patm1987](http://github.com/patm1987) where I keep a number of (mostly incomplete) side projects
* My [LinkedIn Profile](https://www.linkedin.com/in/patrick-martin-268a85a/) which is almost as out of date as this old site
* [Old DigiPen site](https://students.digipen.edu/~pmartin/)
#### What Exactly Happened?
I used a dynamic CMS to serve what should be a static page and this happened:

>We recently completed a routine security checkup of our servers and platforms. Our scans flagged your patrickse.com hosting accounts as containing possible malware.
>
>Please sign in to your hosting account and review the following content and remove or fix the files listed below:
>backup/pat0918006441980_4579189
>html/wp-admin/admin_ver1.php
>html/wp-admin/downloads/spacethings_new.php
>html/wp-admin/images/comment-grey-bubble-2x_bck_old.php
>html/wp-content/uploads/2015/acef9277_ver1.php
>html/wp-includes/certificates/ca-bundle_new.php
>html/wp-includes/js/crop/cropper_old.php
>html/wp-includes/SimplePie/Cache/DB_ver1.php

I don't think I've served up anything terrible, but I don't want to take the chance.
### Table of Contents
{% for post in site.posts %}
* [{{ post.title }}]({{ post.url | prepend: site.github.url}})
{% endfor %}