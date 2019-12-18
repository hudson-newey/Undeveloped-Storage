import java.awt.BorderLayout;
import java.awt.Font;
import javax.swing.*;
import java.awt.*;


class Notepad {
  public static void main(String[] args) {
    Toolkit t = Toolkit.getDefaultToolkit();
    Dimension d = t.getScreenSize();
    JFrame f = new JFrame("Notepad");
    f.setSize(600, 550);
    f.setLocation(300,200);
    final JTextArea textArea = new JTextArea(10, 40);
    f.getContentPane().add(BorderLayout.CENTER, textArea);

    textArea.setSize(d.width, d.height);
    textArea.setFont(new Font("Dialog", Font.TRUETYPE_FONT, 16));
    textArea.setBackground(Color.decode("#282c34"));
    textArea.setForeground(Color.decode("#abb2bf"));
    textArea.setCaretColor(Color.decode("#abb2bf"));

    f.setVisible(true);
  }
}
