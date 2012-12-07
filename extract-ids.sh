# switch to the correct dir
cd /Volumes/sils/users/hemminge/shared/Endeca/Daphne/20110721-20111013/unzipped

# make a file to hold the ids
cd ..
touch ids.txt
cd unzipped

# OSX Mountain Lion has removed -P (allow perl-compatible regex) switch from
# its version of grep. Boo, Apple. Boo.
# So install GNU grep with Homebrew, as shown here: http://news.ycombinator.com/item?id=4841557

brew tap homebrew/dupes
brew install grep

# install super-sed to use perl regexes
brew install ssed

# search the files in this directory and write all the ids to a dedicated file
grep -oP 'UNC\w+\d' * | ssed -R "s/access\.\d+://g" >> ../ids.txt

# there are tons of duplicated IDs in the result file. Get just the unique IDs
# cd. the sort -u method takes forever but the uniq -u method seems to remove stuff
# that isn't a duplicate.
sort -u ids.txt > unique-ids.txt

