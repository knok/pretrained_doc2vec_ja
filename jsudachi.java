import java.io.IOException;
import java.util.*;

import com.worksap.nlp.sudachi.*;
import com.worksap.nlp.sudachi.Dictionary;
import com.worksap.nlp.sudachi.Tokenizer.*;
import py4j.GatewayServer;

public class jsudachi {
    String resourcesDirectory = null;
    static String settings = null;
    boolean mergeSettings = false;
    static Dictionary dict = null;
    static Tokenizer tokenizer = null;
    static Tokenizer.SplitMode mode = Tokenizer.SplitMode.C;

    public List<Morpheme> tokenize(String line) {
        List<Morpheme> morphemeList = tokenizer.tokenize(mode, line);
        return morphemeList;
    }

    public jsudachi() {
        try {
            dict = new DictionaryFactory().create(settings);
            tokenizer = dict.create();
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }
    }

    public static void main(String[] args) {
        jsudachi app = new jsudachi();
        // GatewayServer gateway = new GatewayServer(app);
        GatewayServer gateway = new GatewayServer(app);
        gateway.start();
        System.out.println("Starting server...");
    }
}