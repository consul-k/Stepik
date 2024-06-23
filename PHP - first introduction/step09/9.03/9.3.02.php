interface Reptile {
    public function voice();
}
//пишите свой код ниже
class Snake implements Reptile {
    public function voice() {
        echo "Ш-ш-ш-ш";
    }
}
