if File.file?("sample.txt")
  file = File.open("sample.txt")
  puts file.read
  file.close
else
  puts "Файл не существует"
end
