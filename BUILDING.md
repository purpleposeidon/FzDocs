How To Update The Docs
======================

1. Get a web server running from the root /var/www/html
2. Checkout master, and copy those files into the web root.
3. Create the resources folder, symlinking in minecraft & factorization's assets.
4. Run the /html-fzdoc-export command in Minecraft. Do *not* have any mods other than FZ and its hard dependencies.
5. Run update.sh, in this repository.
6. Add all the files, push to github.
