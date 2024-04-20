import random

nicknames = [
    "Sunny", "Lucky", "Shadow", "Phoenix", "Echo", "Raven", "Ghost", "Breeze", "Blaze", "Mystery",
    "Ace", "Jazz", "Nova", "Dusk", "Vortex", "Sparrow", "Midnight", "Whisper", "Storm", "Falcon",
    "Dragon", "Rocket", "Zenith", "Sapphire", "Stormy", "Viper", "Legend", "Mystic", "Blizzard", "Eclipse",
    "Sky", "Hunter", "Aurora", "Infinity", "Puma", "Thunder", "Orion", "Spectre", "Goblin", "Spirit",
    "Rogue", "Cosmo", "Crimson", "Comet", "Neon", "Phantom", "Volt", "Galaxy", "Pyro", "Pixel",
    "Sage", "Shade", "Titan", "Velocity", "Vortex", "Zephyr", "Abyss", "Aether", "Avalanche", "Bolt",
    "Chaos", "Flare", "Genesis", "Glacier", "Havoc", "Ignite", "Inferno", "Luna", "Magma", "Nebula",
    "Omega", "Pulse", "Quasar", "Rogue", "Solstice", "Solar", "Talon", "Twilight", "Vertex", "Zen",
    "Zodiac", "Amber", "Blitz", "Cascade", "Cobalt", "Enigma", "Frost", "Grim", "Harmony", "Haze",
    "Mystique", "Nimbus", "Obsidian", "Pandora", "Radiance", "Seraph", "Tranquil", "Vortex", "Wraith", "Zenith"
]

def getUsername(userAndWsClientDict):
    unnumber = random.randint(0,99)
    nickname = nicknames[unnumber]
    for userAndWsClient in userAndWsClientDict:
        for key, value in userAndWsClient.items():
            if value == nickname:
                return getUsername(userAndWsClientDict)
    return nickname